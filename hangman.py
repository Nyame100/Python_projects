import random
# This is a hangman game.

# Generate a random word.
words = ["BROWSING","BOY","A", "NAVIGATE","CLICKING","SEARCHES", "QUERYING", "DISCOVER"]
random_word = random.choice(words)
print(random_word)

# Generate blanks matching each word.
word_length = len(random_word)
print("_"*word_length)

# Asking user to guess a word.
guess = input("Guess a letter\n")
