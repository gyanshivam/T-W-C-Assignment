"""
CodeMate: A rule‑based chatbot for beginner programmers.
Helps with Python basics, debugging, and learning resources.
"""

import re
import random

# Greeting variations
GREETINGS = [
    "Hey there! I'm CodeMate. Ready to code? 🐍",
    "Welcome! I'm your Python buddy. Ask me anything.",
    "Hi! CodeMate here. Need help with variables, loops, or functions?"
]

# Farewell messages
FAREWELLS = [
    "Happy coding! See you next time.",
    "Keep practicing. CodeMate out! 👋",
    "Goodbye! Remember, every expert was once a beginner."
]

# Help menu content
HELP_TEXT = """
🤖 *CodeMate Commands* 🤖
----------------------------------------
- "hello" / "hi"         → Greet the bot
- "help"                 → Show this menu
- "explain <topic>"      → Get explanation (e.g., explain loops)
- "debug"                → Tips for fixing errors
- "code <concept>"       → Show a small code example (e.g., code function)
- "resource"             → Recommended learning links
- "joke"                 → A programming joke 😄
- "bye" / "exit"         → End conversation
"""

# Explanation patterns
EXPLANATIONS = {
    r"variable": (
        "A variable is like a labeled box where you store data. "
        "Example: `age = 25` stores the number 25 in the variable 'age'."
    ),
    r"loop|for|while": (
        "Loops repeat a block of code. `for` iterates over a sequence, "
        "`while` runs until a condition becomes False.\n"
        "Example: `for i in range(3): print(i)` prints 0,1,2."
    ),
    r"function|def": (
        "A function is a reusable block of code. Define with `def`.\n"
        "Example: `def greet(name): return f'Hello {name}'`"
    ),
    r"list": (
        "A list stores multiple items in one variable. "
        "Example: `fruits = ['apple', 'banana']`. Index starts at 0."
    ),
    r"dictionary|dict": (
        "A dictionary stores key‑value pairs. Example: `person = {'name': 'Alice', 'age': 25}`."
    ),
    r"if|else|conditional": (
        "Conditionals let your code make decisions.\n"
        "Example: `if score >= 60: print('Pass') else: print('Fail')`"
    ),
}

# Code snippets for common requests
CODE_SAMPLES = {
    "function": "def add(a, b):\n    return a + b\n\nresult = add(3, 5)\nprint(result)  # 8",
    "loop": "for i in range(1, 6):\n    print(f'Count: {i}')",
    "list": "colors = ['red', 'green', 'blue']\nfor color in colors:\n    print(color)",
    "if": "temperature = 30\nif temperature > 25:\n    print('It's hot!')\nelse:\n    print('It's cool.')",
    "input": "name = input('What is your name? ')\nprint(f'Hello {name}!')",
}

# Debugging tips
DEBUG_TIPS = [
    "🐞 Read the error message carefully – it tells you the line number and what's wrong.",
    "🐞 Use `print()` statements to check variable values at different points.",
    "🐞 Check for missing colons `:` after `if`, `for`, `def`.",
    "🐞 Indentation matters! Use 4 spaces consistently.",
    "🐞 Make sure you didn't misspell variable names (case‑sensitive)."
]

# Programming jokes
JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "How many programmers does it take to change a light bulb? None – that's a hardware problem.",
    "Why did the Python developer break up with the list? Because it had too many 'except'ions.",
    "What's a programmer's favorite hangout? The Foo Bar."
]

# Learning resources
RESOURCES = [
    "📘 Python Official Tutorial: https://docs.python.org/3/tutorial/",
    "🎓 W3Schools Python: https://www.w3schools.com/python/",
    "🐍 Real Python: https://realpython.com/",
    "💡 freeCodeCamp Python Course: https://www.youtube.com/watch?v=rfscVS0vtbw"
]

def normalize(text):
    """Convert to lowercase and remove extra spaces."""
    return re.sub(r'\s+', ' ', text.strip().lower())

def get_explanation(text):
    """Return explanation for a keyword if found."""
    for pattern, explanation in EXPLANATIONS.items():
        if re.search(pattern, text):
            return explanation
    return None

def main():
    print("🐍 *CodeMate Chatbot* - Your Python learning companion")
    print("Type 'help' to see what I can do, or 'bye' to exit.\n")
    
    # Get user's name (optional)
    name_input = input("What should I call you? ").strip()
    name = name_input if name_input else "Friend"
    print(f"\nNice to meet you, {name}! Let's learn Python.\n")
    
    while True:
        user_input = input(f"{name} > ")
        if not user_input:
            continue
        
        cmd = normalize(user_input)
        
        # Exit conditions
        if cmd in ("bye", "exit", "quit", "goodbye"):
            print(random.choice(FAREWELLS))
            break
        
        # Greetings
        elif cmd in ("hello", "hi", "hey", "greetings"):
            print(random.choice(GREETINGS))
        
        # Help menu
        elif cmd == "help":
            print(HELP_TEXT)
        
        # Explain concept
        elif cmd.startswith("explain"):
            topic = cmd.replace("explain", "").strip()
            if not topic:
                print("What would you like me to explain? (e.g., 'explain loops')")
            else:
                explanation = get_explanation(topic)
                if explanation:
                    print(f"📖 {explanation}")
                else:
                    print("Sorry, I don't have an explanation for that yet. Try: variables, loops, functions, lists, dictionaries, or conditionals.")
        
        # Code example
        elif cmd.startswith("code"):
            concept = cmd.replace("code", "").strip()
            if not concept:
                print("Which concept? Try: 'code function', 'code loop', 'code list', 'code if', 'code input'")
            else:
                for key in CODE_SAMPLES:
                    if key in concept:
                        print(f"💻 Code example for {key}:\n```python\n{CODE_SAMPLES[key]}\n```")
                        break
                else:
                    print("I have examples for: function, loop, list, if, input. Please specify one.")
        
        # Debugging tips
        elif cmd == "debug":
            print("🛠️ *Debugging Tips*")
            print(random.choice(DEBUG_TIPS))
        
        # Joke
        elif cmd == "joke":
            print(f"😂 {random.choice(JOKES)}")
        
        # Learning resources
        elif cmd == "resource":
            print("📚 *Recommended Learning Resources*")
            for res in RESOURCES:
                print(f"  {res}")
        
        # Unknown command
        else:
            print("I'm not sure how to help. Try 'help' for available commands.")
            print("You can also ask me to 'explain' a topic (e.g., 'explain loops') or 'code' an example (e.g., 'code function').")

if __name__ == "__main__":
    main()