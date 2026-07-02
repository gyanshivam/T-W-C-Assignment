import random

# Small talk responses
greetings = ["Hey there!", "Hi!", "Hello!", "Greetings!"]
farewells = ["Goodbye!", "See you later!", "Take care!", "Bye!"]

print(random.choice(greetings))
print("I'm your AI assistant. What's your name?")
name = input("> ").strip()
print(f"Nice to meet you, {name}! I'm here to chat or answer simple questions.")

# Main conversation loop
while True:
    print("\nYou can ask me about weather, tell me how you feel, or say 'bye' to exit.")
    user_input = input(f"{name}: ").lower().strip()
    
    if user_input in ["bye", "goodbye", "exit", "quit"]:
        print(random.choice(farewells))
        break
    
    elif "weather" in user_input:
        print("I don't have live weather data, but I hope it's sunny where you are!")
    
    elif "feel" in user_input or "mood" in user_input:
        if "happy" in user_input or "good" in user_input:
            print("That's awesome! Keep smiling 😊")
        elif "sad" in user_input or "bad" in user_input:
            print("Sorry to hear that. Remember, tough times don't last.")
        else:
            print("I understand. Feelings can be complicated.")
    
    elif "name" in user_input:
        print(f"Your name is {name}, and I'm your AI buddy.")
    
    elif "help" in user_input:
        print("You can ask me about weather, your mood, or just say 'bye' to end.")
    
    else:
        responses = [
            "Interesting! Tell me more.",
            "I'm still learning. Could you rephrase?",
            "Hmm, that's beyond my current knowledge.",
            "Cool! Let's talk about something else."
        ]
        print(random.choice(responses))

print(f"Thanks for chatting, {name}. See you next time!")