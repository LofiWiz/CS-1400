# Seth Mitchell (10600367)
# CS 1400
# exercise 4.3

# program to calculate speeding fines
# inputs
print("this is a program to calculate speeding fines, please enter the information requested")
speed_limit = float(input("please enter the speed limit: "))
speed_going = float(input("please enter the speed travelling: "))

# logic and bool; determining fine amount
if speed_going <= speed_limit:
    print("speed is legal")
elif speed_going > speed_limit and speed_going <= 90:
    fine = (50 + 5 * (speed_going - speed_limit))
    print(f"speed is illegal; fine is ${fine:.2f}.")
elif speed_going > speed_limit and speed_going > 90:
    fine = (50 + 5 * (speed_going - speed_limit) + 200)
    print(f"speed is illegal; fine is ${fine:.2f}.")
