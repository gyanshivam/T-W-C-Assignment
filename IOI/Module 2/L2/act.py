# ---- Music Playlist Matcher ----

# STEP 1 - Create tuples for playlist details (fixed — cannot be changed)
chill_hop = ("Lo-Fi Chill", "Lo-Fi", 55, "Relaxed")
workout = ("Power Gym Mix", "EDM", 40, "High Energy")
print("Playlist 1:", chill_hop)
print("Name:", chill_hop[0])
print("Genre:", chill_hop[1])
print("Mood:", chill_hop[-1])

# STEP 2 - Nested tuples and slicing
all_playlists = (chill_hop, workout)
print("\nFirst playlist name:", all_playlists[0][0])
print("Second playlist duration:", all_playlists[1][2], "mins")
print("Chill Hop details (sliced):", chill_hop[1:3])

# STEP 3 - Iterate through a tuple
print("\nChill Hop details:")
for info in chill_hop:
    print(" -", info)

# STEP 4 - Create sets for songs (no duplicates allowed)
chill_songs = {"Sunset Drive", "Rainy Window", "Coffee Break", "Night Walk", "Cloud Nine", "Sunset Drive"}
gym_songs = {"Beast Mode", "Adrenaline", "Night Walk", "Fire Up", "Power Surge", "Ignite"}
print("\nChill songs:", chill_songs)
print("Gym songs:", gym_songs)
print("Total chill tracks:", len(chill_songs))

# STEP 5 - Modify the set
chill_songs.add("Moonlight")
chill_songs.discard("Coffee Break")
print("\nUpdated chill songs:", chill_songs)

# STEP 6 - Set operations
combined_tracks = chill_songs.union(gym_songs)
shared_tracks = chill_songs.intersection(gym_songs)
only_chill = chill_songs.difference(gym_songs)
exclusive_tracks = chill_songs.symmetric_difference(gym_songs)

print("\nAll tracks (union):", combined_tracks)
print("Shared tracks (intersection):", shared_tracks)
print("Only in Chill (difference):", only_chill)
print("Not shared (sym. difference):", exclusive_tracks)