# Sentiment Spy - AI Mission: Decode Emotions
# A unique implementation using TextBlob with a spy theme

import sys
from textblob import TextBlob

# Check if textblob is installed (optional instruction)
try:
    from textblob import TextBlob
except ImportError:
    print("Please install textblob: pip install textblob")
    sys.exit(1)

# Mission intro
print("\n🔍🔐 * * * SENTIMENT SPY - SECRET MISSION * * * 🔐🔍")
print("Greetings, Agent. Your task: decode the emotional signature of any message.")
print("Our AI will classify sentiment as Positive, Neutral, or Negative.\n")

agent_name = input("What is your SpyWorldName? ").strip() or "Shadow"
print(f"\n🤖 AI: Welcome, Agent {agent_name}. Ready to spy on emotions?")

# Dictionary to store mission logs
mission_log = []

# Main loop
while True:
    print("\n" + "-" * 50)
    encrypted_msg = input(f"{agent_name} > Enter your message (or type 'report', 'clear', 'abort'): ").strip()
    
    if not encrypted_msg:
        print("🕵️ No message detected. Please send a text.")
        continue
    
    cmd = encrypted_msg.lower()
    if cmd == "abort":
        print(f"\n🚪 Mission terminated. Goodbye, Agent {agent_name}.\n")
        break
    elif cmd == "clear":
        mission_log.clear()
        print("📋 Mission log cleared. All previous analyses erased.")
        continue
    elif cmd == "report":
        if not mission_log:
            print("📭 No messages analyzed yet. Send a message first.")
        else:
            print("\n📊 MISSION REPORT:")
            for i, (text, sentiment, polarity) in enumerate(mission_log, 1):
                emoji = "😊" if sentiment == "Positive" else ("😞" if sentiment == "Negative" else "😐")
                print(f"  {i}. {emoji} \"{text[:50]}{'...' if len(text)>50 else ''}\" -> {sentiment} (score: {polarity:.2f})")
        continue
    
    # Sentiment analysis using TextBlob
    blob = TextBlob(encrypted_msg)
    polarity = blob.sentiment.polarity  # range -1 to 1
    
    # Determine sentiment with three levels (positive > 0.1, negative < -0.1, neutral otherwise)
    if polarity > 0.1:
        sentiment = "Positive"
        emoji = "😊"
        color_prefix = "\033[92m"  # Green
    elif polarity < -0.1:
        sentiment = "Negative"
        emoji = "😞"
        color_prefix = "\033[91m"  # Red
    else:
        sentiment = "Neutral"
        emoji = "😐"
        color_prefix = "\033[93m"  # Yellow
    
    # Store in mission log
    mission_log.append((encrypted_msg, sentiment, polarity))
    
    # Decode result
    print(f"{color_prefix}🤖 AI Analysis: {emoji} {sentiment} sentiment detected.")
    print(f"   Emotional polarity score: {polarity:.3f} (from -1 to +1){Style.RESET_ALL if 'Style' in dir() else ''}")
    
    # Provide mission-themed feedback
    if sentiment == "Positive":
        print("   💪 Positive energy detected. Your message boosts morale!")
    elif sentiment == "Negative":
        print("   🚨 Negative signal. Proceed with caution – may require support.")
    else:
        print("   🕶️ Neutral reading. No strong emotional signature.")

# Note: color codes are ANSI escape sequences; they work in most terminals.
# If you prefer no colors, remove the color_prefix and reset.

print("\n🔒 Sentiment Spy mission complete. You've explored how AI processes data to detect emotions.")
print("  Key concepts: sentiment analysis, polarity scoring, real‑time classification.")