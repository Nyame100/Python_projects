line1 = ["X", "X", "X"]
line2 = ["X", "X", "X"]
line3 = ["X", "X", "X"]

map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")

position = input("Where do you want to put your treaure ?\n")
#cordinates = [position[0], position[1]]

#if position[1] == "3" and position[0] == "A":
#    line3[0] = "Y"


if position[0] == "A":
    if position[1] == "3":
        line3[0] = "Y"
    elif position[1] == "2":
        line2[0] = "Y"
    else:
        line1[0] = "Y"
elif position[0] == "B":
    if position[1] == "3":
        line3[1] = "Y"
    elif position[1] == "2":
        line2[1] = "Y"
    else:
        line1[1] = "Y"
else:
    if position[1] == "3":
        line3[2] = "Y"
    elif position[1] == "2":
        line2[2] = "Y"
    else:
        line1[2] = "Y"

#print(position[0],position[1])
print(f"{line1}\n{line2}\n{line3}")

#print(cordinates)
