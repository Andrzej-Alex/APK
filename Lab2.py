"""
Andrzej Aleksandrowicz4
"""

# 1)

while True:
    x = int(input("Wprowadź pierwszą liczbę: "))
    y = int(input("Wprowadź drugą liczbę: "))
    if x == 0 or y == 0:
        print("Zatrzymanie programu z powodu: x lub y jest ZEREM")
        break
    product = x * y
    print(f"{x} * {y} = {product}")
    print("Do you want to continue? (y/n)")
    answer = input()
    if answer == "n":
        print("Program stopped working")