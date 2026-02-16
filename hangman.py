import random
# This is a hangman game.

# Generate a random word.
words = ["BROWSING","BOY","A", "NAVIGATE","CLICKING","SEARCHES", "QUERYING", "DISCOVER"]
random_word = random.choice(words)
print(random_word)

# Generate blanks matching each word.
word_length = len(random_word)
blanks = list("_"*word_length)
print(" ".join(blanks))
print(blanks)
# Asking user to guess a word.
guessed_letter = input("Guess a letter\n").upper()

# Checking if letter is in word.
for i in range(len(random_word)):
    i_occurence = []
    if random_word[i] == guessed_letter:
        i_occurence.append(i)
        blanks[i] = guessed_letter
        print(blanks)
        print(" ".join(blanks))
