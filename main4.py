#import random

#random_integer = random.randint(1, 10)
#print(random_integer)

#random_float = random.random()
#print(random_float*5)


#fruits = ["Strawberries", "Nectarines", "Apples"]
#
#vegetables = ["Spinach", "Kale", "Tomatoes"]
#
#dirty_dozen = [fruits, vegetables]
#print(dirty_dozen)



# Average student height

#student_heights = input("Enter a list of student heights\n").split()

#for n in range(0, len(student_heights)):
#    student_heights[n] = int(student_heights[n])
#total_height = 0
#total_stu = 0
#for height in student_heights:
#    total_height += height
#    total_stu += 1
#    avr_height = total_height/total_stu
#print(avr_height)

total = 0
for number in range(1,101):
    total += number
print(total)
