import random

names_string = input("Write the names of your friends separated by ','\n")
names = names_string.split(", ")

# Get the total number of items in the list.
number_of_people = len(names)

# Generate random numbers between 0 and the last index.
integer = number_of_people - 1
random_number = random.randint(0,integer)

# Pick out random person from list of names using the random number.
pick = names[random_number]
print(f"{pick} is going to buy the meal today!")


