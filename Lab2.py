"""
Andrzej Aleksandrowicz
"""

# 1)

while True:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    if x == 0 or y == 0:
        print("Program stopped working because either x or y is 0")

        break

    product = x * y

    print(f"{x} * {y} = {product}")
    print("Do you want to continue? (y/n)")
    answer = input()
    if answer == "n":
        print("Program stopped working")