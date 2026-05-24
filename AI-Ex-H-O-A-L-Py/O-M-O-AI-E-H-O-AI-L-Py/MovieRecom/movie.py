
# Download the IMDB Top 1000 dataset
import kagglehub
import pandas as pd
import os

# Download the dataset
path = kagglehub.dataset_download("harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows")
print("Path to dataset files:", path)

# Find the CSV file in the downloaded path
for file in os.listdir(path):
    if file.endswith(".csv"):
        csv_path = os.path.join(path, file)
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_path)
        # Save it to the current Colab environment with a simpler name
        df.to_csv("imdb_top_1000.csv", index=False)
        print("File saved as 'imdb_top_1000.csv'")
        break

# Actual Program

"""
AI Movie Recommendation System
--------------------------------
This program loads the IMDB Top 1000 movies dataset and recommends movies
based on:
- Genre preference
- Minimum IMDB rating
- User's current mood (sentiment analysis on user's text)
It uses:
- pandas for data handling
- textblob for sentiment analysis
- colorama for coloured terminal output
"""

import pandas as pd
import random
import time
from textblob import TextBlob
from colorama import init, Fore, Style

# Initialize colorama for cross‑platform coloured output
init(autoreset=True)

# ------------------------------------------------------------
# 1. Load and prepare the dataset
# ------------------------------------------------------------
def load_data(filepath="imdb_top_1000.csv"):
    """Load the CSV file and return a DataFrame."""
    try:
        df = pd.read_csv(filepath)
        # Keep only relevant columns
        df = df[['Series_Title', 'Genre', 'IMDB_Rating', 'Overview']]
        # Drop rows with missing values
        df.dropna(inplace=True)
        # Ensure rating is float
        df['IMDB_Rating'] = df['IMDB_Rating'].astype(float)
        print(Fore.GREEN + f"✅ Loaded {len(df)} movies successfully.")
        return df
    except FileNotFoundError:
        print(Fore.RED + f"❌ Error: File '{filepath}' not found.")
        print(Fore.YELLOW + "Please place 'imdb_top_1000.csv' in the same folder as this script.")
        exit(1)
    except Exception as e:
        print(Fore.RED + f"❌ Unexpected error loading data: {e}")
        exit(1)


# ------------------------------------------------------------
# 2. Helper functions
# ------------------------------------------------------------
def extract_genre_list(df):
    """Extract all unique genres from the 'Genre' column (split by comma)."""
    genres = set()
    for g in df['Genre'].dropna():
        for genre in g.split(', '):
            genres.add(genre.strip())
    return sorted(genres)


def display_genres(genres):
    """Show numbered list of available genres."""
    print(Fore.CYAN + "\n🎭 Available Genres:")
    for idx, genre in enumerate(genres, start=1):
        print(f"   {idx}. {genre}")
    print()


def get_genre_choice(genres):
    """Let user pick a genre by number or name."""
    while True:
        choice = input(Fore.YELLOW + "Choose a genre (number or name): " + Style.RESET_ALL).strip()
        # Try as number
        if choice.isdigit():
            num = int(choice)
            if 1 <= num <= len(genres):
                return genres[num-1]
        # Try as name
        if choice.title() in genres:
            return choice.title()
        print(Fore.RED + "Invalid choice. Please try again.")


def get_rating_filter():
    """Ask user for minimum IMDB rating (optional)."""
    print(Fore.CYAN + "\n⭐ IMDB Rating Filter (optional)")
    print("   Range: 7.6 - 9.3 (or press Enter to skip)")
    while True:
        inp = input(Fore.YELLOW + "Minimum rating: " + Style.RESET_ALL).strip()
        if inp == "":
            return None
        try:
            rating = float(inp)
            if 7.6 <= rating <= 9.3:
                return rating
            else:
                print(Fore.RED + "Rating must be between 7.6 and 9.3.")
        except ValueError:
            print(Fore.RED + "Please enter a number or press Enter.")


def analyze_mood(user_text):
    """Return polarity and sentiment label."""
    blob = TextBlob(user_text)
    polarity = blob.sentiment.polarity  # range -1 to 1
    if polarity > 0.2:
        sentiment = "Positive 😊"
    elif polarity < -0.2:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"
    return polarity, sentiment


def animated_loading(message, duration=1.5):
    """Show a simple animated loading effect."""
    print(Fore.MAGENTA + message, end="", flush=True)
    for _ in range(3):
        time.sleep(0.4)
        print(Fore.YELLOW + ".", end="", flush=True)
    print(Style.RESET_ALL)


# ------------------------------------------------------------
# 3. Recommendation engine
# ------------------------------------------------------------
def recommend_movies(df, genre, min_rating, mood_polarity, top_n=5):
    """
    Filter movies by genre and rating, then sort by:
    - Sentiment polarity of overview (positive > neutral > negative)
    - Additional randomness to avoid same list every time.
    Returns a list of tuples (title, overview_polarity, rating).
    """
    # Filter by genre
    filtered = df[df['Genre'].str.contains(genre, case=False, na=False)]
    # Filter by rating
    if min_rating is not None:
        filtered = filtered[filtered['IMDB_Rating'] >= min_rating]
    
    if filtered.empty:
        return []
    
    # Compute sentiment polarity for each movie's overview
    filtered = filtered.copy()
    filtered['Overview_Polarity'] = filtered['Overview'].apply(
        lambda x: TextBlob(x).sentiment.polarity
    )
    
    # Custom sorting: prefer movies whose overview sentiment matches user's mood
    # (positive mood -> higher overview polarity, negative mood -> lower polarity)
    if mood_polarity > 0.2:
        # User is happy -> prefer positive overviews
        filtered = filtered.sort_values('Overview_Polarity', ascending=False)
    elif mood_polarity < -0.2:
        # User is sad -> prefer negative overviews (maybe dramatic movies?)
        filtered = filtered.sort_values('Overview_Polarity', ascending=True)
    else:
        # Neutral mood -> sort by rating first, then randomize a bit
        filtered = filtered.sort_values('IMDB_Rating', ascending=False)
    
    # Add a small random factor to avoid identical lists
    filtered = filtered.sample(frac=1, random_state=None).reset_index(drop=True)
    
    # Return top N
    results = []
    for _, row in filtered.head(top_n).iterrows():
        results.append((row['Series_Title'], row['Overview_Polarity'], row['IMDB_Rating']))
    return results


def display_recommendations(movies, user_name):
    """Pretty‑print the list of recommended movies."""
    if not movies:
        print(Fore.RED + "😞 No movies match your criteria. Try different filters.")
        return
    
    print(Fore.GREEN + f"\n🎬 {user_name}, here are your personalized recommendations:\n")
    for i, (title, pol, rating) in enumerate(movies, 1):
        # Emoji based on polarity
        emoji = "😊" if pol > 0 else ("😞" if pol < 0 else "😐")
        print(f"   {Fore.CYAN}{i}. {Fore.YELLOW}{title} {emoji}")
        print(f"      {Fore.WHITE}IMDB: {rating:.1f}  |  Overview Polarity: {pol:.2f}")
    print()


# ------------------------------------------------------------
# 4. Main interactive loop
# ------------------------------------------------------------
def main():
    print(Fore.BLUE + "=" * 60)
    print(Fore.CYAN + "   🎥 AI MOVIE RECOMMENDATION SYSTEM 🎥")
    print(Fore.BLUE + "=" * 60)
    
    # Load data
    df = load_data()
    genres = extract_genre_list(df)
    
    # Get user name
    user_name = input(Fore.YELLOW + "\nWhat's your name? " + Style.RESET_ALL).strip()
    if not user_name:
        user_name = "Movie Lover"
    print(Fore.GREEN + f"\nHello {user_name}! Let's find your perfect movie.\n")
    
    # Get genre
    display_genres(genres)
    selected_genre = get_genre_choice(genres)
    print(Fore.GREEN + f"Selected genre: {selected_genre}\n")
    
    # Get rating filter
    min_rating = get_rating_filter()
    if min_rating:
        print(Fore.GREEN + f"Filtering movies with rating ≥ {min_rating}\n")
    
    # Get mood
    print(Fore.CYAN + "🎭 How are you feeling today?")
    mood_text = input(Fore.YELLOW + "Describe your mood: " + Style.RESET_ALL).strip()
    if not mood_text:
        mood_text = "neutral"
    animated_loading("Analyzing your mood", 1.2)
    polarity, sentiment = analyze_mood(mood_text)
    print(Fore.MAGENTA + f"Detected mood: {sentiment} (polarity: {polarity:.2f})\n")
    
    # Get recommendations
    animated_loading("Searching for movies", 1.5)
    recs = recommend_movies(df, selected_genre, min_rating, polarity, top_n=5)
    
    if recs:
        display_recommendations(recs, user_name)
    else:
        print(Fore.RED + "No recommendations found. Please try different filters.")
    
    # Optional: ask for more recommendations
    while True:
        more = input(Fore.YELLOW + "Would you like more recommendations? (yes/no): " + Style.RESET_ALL).strip().lower()
        if more == 'no':
            print(Fore.GREEN + f"\nEnjoy your movie night, {user_name}! 🍿✨\n")
            break
        elif more == 'yes':
            # Use same filters but get next set? We can re‑run with different random shuffle
            new_recs = recommend_movies(df, selected_genre, min_rating, polarity, top_n=5)
            if new_recs:
                # Avoid repeating same movies if possible
                existing_titles = {t for t, _, _ in recs}
                fresh = [m for m in new_recs if m[0] not in existing_titles]
                if not fresh:
                    fresh = new_recs[:3]  # fallback
                display_recommendations(fresh, user_name)
                recs.extend(fresh)  # update to avoid repeats next time
            else:
                print(Fore.RED + "No additional movies found.")
        else:
            print(Fore.RED + "Please answer 'yes' or 'no'.")


if __name__ == "__main__":
    main()