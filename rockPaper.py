import random

print("This is Rock Paper Scissors game!\n")

#This is the user input- The user chooses a number.
user_number = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''    

paper = '''
    _______
---'   ____)____
          ______)
          _______)
          _______)
---.__________)

'''

scissors = '''

   _______
---'   ____)____
          ______)
        __________)
      (____)
---.__(___)

'''

# Defining a list whose indices will match to users chosen number.
choice = [rock,paper,scissors]

# Generating random numbers.
cpu_number = random.randint(0,2)

# Coverting the user choice and cpu choice into concatenated string - to preserve the individual values when i put them together.
point = str(user_number)+str(cpu_number)

# Catching potential errors.
if user_number > 2 or user_number < 0:
    print(f"You entered an invalid number {user_number}! choose btw 0-2")
else:
    print(f"You chose:\n{choice[user_number]}")
    print(f"CPU chose:\n{choice[cpu_number]}")


    # Defining the winning, draw and losing rules.
    if point == "02" or point == "21" or point == "10":
        print("You win")
    elif point == "00" or point == "11" or point == "22":
        print("Draw game")
    else:
        print("You lose!!!")
    print(user_number, cpu_number)
