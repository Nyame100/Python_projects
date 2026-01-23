line1 = ["X", "X", "X"]
line2 = ["X", "X", "X"]
line3 = ["X", "X", "X"]

map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")

position = input("Where do you want to put your treaure ?\n")
letter_cor = position[0].lower()
number_cor = int(position[1])

letters = ["a", "b","c"]
letter_ind = letters.index(letter_cor)
number_ind = number_cor - 1
map[number_ind][letter_ind] = "Y"
print(f"{line1}\n{line2}\n{line3}")

