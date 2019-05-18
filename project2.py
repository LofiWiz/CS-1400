# Seth Mitchell (10600367)
# CS 1400
# Project 2: A day on the farm
# Simulator to determine if a farmer must water crops, harvest and sell crops,
# or if he will have enough time to  treat friends to a dinner; restricted to only doing 2 of the 3

import random
#account opening balance
balance = float(input("please enter current balance: "))

# bool 1; determining the weather; for if crops need to be watered
if random.randrange(1,5) == 1:
    weather = str("rainy")
    print("because of the rain, you didn't need to water your crops")
else:
    weather = str("no rain")
    print("their was no rain and you had to water your crops!")
    
# bool 2; determining if crops should be harvested and sold
if random.randrange(1,6) == 1:
    crops = str("harvested and sold")
    income = float(random.randrange(100,201))
    print(f"you harvested and sold your crops for ${income:.2f}!")
else:
    crops = str("not ready")
    print("your crops were not ready for harvesting")
    income = 0

# bool 3; determining if a thank you dinner is a viable option;
# can't have harvested + watered, and must have a balance >= 60
if weather == str("no rain") and crops == str("harvested and sold"):
    print("you had to water your crops and harvested and sold them!")
    print("you didn't have enough time for the thank you dinner!")
    ending_balance = balance + income
    print(f"your balance at the end of the day is ${ending_balance:.2f}!")
elif (weather == str("rainy") or crops == str("not ready")) and (balance + income >= 60):
    print("you had enough time for the dinner! It was wonderful and cost $60.00!")
    ending_balance = balance + income - 60
    print(f"your balance at the end of the day is ${ending_balance:.2f}!")
else:
    print("you had enough time for the thank you dinner, however,")
    print("you need at least $60.00 for the thank you dinner for your friends!")
    print("you are unable to have the thank you dinner")
    ending_balance = balance + income
    print(f"your balance at the end of the day is ${ending_balance:.2f}!")

# Some of the things that I learned about during this project was how to use the import random module,
# as well as learning how to assign variables to strings, which I hadn't used in previous assignments.