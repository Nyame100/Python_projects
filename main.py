# BMI Calculator

#BMI = weight(kg) / height²(m²)

#weight_in_kg = float(input("what is your weight ?\n"))
#height_in_m = float(input("what is your height ?\n"))

#BMI = print(f"Your BMI is: {weight_in_kg // height_in_m**2}")




# Weeks of Life

#number_of_weeks_in_year = 52
#avg_age_of_life = 90
# weeks_in_avg_age_life = number_of_weks_in_year * avg_age_of_life

#age = int(input("What is your age ?\n"))
#remaining_years_of_life = avg_age_of_life - age
#life_weeks_left = number_of_weeks_in_year * remaining_years_of_life
#print(f"You have {life_weeks_left} weeks left")



            #DAY3

#Even or Odd number

#number = int(input("Which number do you want to check ?\n"))
#if number % 2 == 0:
#    print(f"{number} is an even number")
#else:
#    print(f"{number} is an odd number")



print("Welcome to the rollercoaster")
height = int(input("What is your height in cm ?\n"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you ? "))
    if age < 12:
        bill += 5
        print(f"Child tickets are ${bill}")
    elif age <= 18:
        bill += 7
        print(f"Youth tickets are ${bill}")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill += 12
        print(f"Adult tickets are ${bill}")

    wants_photo = input("Do you want a photo taken ? Y or N\n")
    if wants_photo == "Y":
        bill += 3
    
    print(f"Your total bill is ${bill}")
    
else:
    print("You are not allowed to ride the rollercoaster")


#BMI calculator 2.0

#height = float(input("what is your height in m ?\n"))
#weight = float(input("What is your weight in kg ?\n"))
#BMI = round(weight/ (height ** 2),1)
#print(BMI)
#if BMI < 18.5:
#    print("You are underweight")
#elif BMI < 25:
#    print("You are normal weight")
#elif BMI < 30:
#    print("You are slightly overweight")
#elif BMI < 35:
#    print("You are obese")
#else:
#    print("You are clinically obese")


#Leap Year Decider

#year = int(input("Which year do you want to check ?\n"))
#
#if year % 4 == 0:
#    if year % 100 == 0:
#        if year % 400 == 0:
#            print(f"{year} is a leap year.")
#        else:
#            print(f"{year} is not a leap year.")
#    else:
#        print(f"{year} is a leap year.")
#else:
#    print(f"{year} is not a leap year.")


