print("The Love Calculator is calculating your score...")
name1 = input("What is your name ?\n")
name2 = input("What is your name ?\n")
true = 0
love = 0
name1_list = list(name1.lower())
name2_list = list(name2.lower())
name_char = name1_list + name2_list

true = ["t", "r", "u", "e"]
love = ["l", "o", "v", "e"]
total1 = 0
total2 = 0
lovescore = 0

for i in true:
    count = name_char.count(i)
    total1 += count
    print(f"{i.upper()} occurs {count} times")
print(f"Total = {total1}")

for i in love:
    count = name_char.count(i)
    total2 += count
    print(f"{i.upper()} occurs {count} times")
print(f"Total = {total2}")
lovescore_str = str(total1)+str(total2)
lovescore = int(lovescore_str)


if lovescore < 10 or lovescore > 90:
    print(f"Your score is {lovescore}, you go together like coke and mentos.")
elif lovescore >= 40 and lovescore <= 50:
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}")

