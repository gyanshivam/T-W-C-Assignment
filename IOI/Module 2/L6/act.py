class EBook:
    def __init__(self, title, rating):
        self.__title = title        # private attribute
        self.__rating = rating      # private attribute

    def info(self):                 # same method name as AudioBook
        print(f"EBook   — Title: {self.__title}, Rating: {self.__rating}/5")

    def engage(self):               # same method name, different output
        print(f"You swipe through '{self.__title}' on your e-reader.")

    def get_rating(self):           # getter — read private data
        return self.__rating

    def set_rating(self, new_rating):  # setter — update private data safely
        if 1 <= new_rating <= 5:
            self.__rating = new_rating
            print(f"Rating updated to {self.__rating}/5")
        else:
            print("Rating must be between 1 and 5.")


class AudioBook:
    def __init__(self, title, rating):
        self.__title = title
        self.__rating = rating

    def info(self):                 # same name, different output
        print(f"AudioBook — Title: {self.__title}, Rating: {self.__rating}/5")

    def engage(self):               # same name, different behaviour
        print(f"You listen to '{self.__title}' through your headphones.")

    def get_rating(self):
        return self.__rating

    def set_rating(self, new_rating):
        if 1 <= new_rating <= 5:
            self.__rating = new_rating
            print(f"Rating updated to {self.__rating}/5")
        else:
            print("Rating must be between 1 and 5.")


# Create objects
ebook = EBook("Python Basics", 4)
audiobook = AudioBook("AI Revolution", 5)

# Polymorphism — same method, different behaviour
print("=== Library Media Tracker ===\n")
for media in (ebook, audiobook):
    media.info()
    media.engage()
    print()

# Encapsulation — direct change does NOT work
print("--- Direct change attempt ---")
ebook.__rating = 10
print(f"get_rating() still shows: {ebook.get_rating()}")

# Setter — the only safe way to update
print("\n--- Updating ratings ---")
ebook.set_rating(5)
audiobook.set_rating(3)