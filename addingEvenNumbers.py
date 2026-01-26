# A program that calculates the sum of all even numbers from 1 to x.

target = int(input("Enter a number between 0 and 1000\n"))

sum_even = 0
for number in range(0,target+1):
    if number % 2 == 0:
        sum_even += number
print(sum_even)
