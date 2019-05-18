# Seth Mitchell (10600367)
# CS 1400
# exercise 4.3

# program to determin eligibility for senate/house of rep. based on age
# inputs
print("this program determines eligibility for house of representatives and senate")
user_age = int(input("please enter your age: "))
user_years_cit = int(input("please enter the number of years of citizenship held: "))

# boolean and logic for eligibility
if user_age >= 30 and user_years_cit >= 9:
    print("eligible for both senate and house of representatives")
elif (user_age >= 25 or user_age < 30) and (user_years_cit >= 7):
    print("eligible for house of representatives")
else:
    print("not eligible for either")
