# Seth Mitchell (10600367)
# CS 1400
# exercise 1

# Chaos Program
print("This program illustrates a chaotic function.")
x = float(input("Enter a number between 0 and 1: "))
for i in range(10):
    x = 3.9 * x * (1 - x)
    print(x)