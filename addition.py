import random as rnd

def add(n1,n2):
    answer = n1 + n2
    print(n1, "+", n2)

    user_input = int(input("Enter Answer : "))

    if answer == user_input:
        print("Correct")
    else:
        print("Incorrect")

def subtract(n1,n2):
    answer = n1 - n2
    print(n1, "-", n2)

    user_input = int(input("Enter Answer : "))

    if answer == user_input:
        print("Correct")
    else:
        print("Incorrect")

def multiply(n1,n2):
    answer = n1 * n2
    print(n1, "x", n2)

    user_input = int(input("Enter Answer : "))

    if answer == user_input:
        print("Correct")
    else:
        print("Incorrect")     


num_01 = rnd.randint(1,9)
num_02 = rnd.randint(1,9)
print("Here are the operations you can pick from. Type the number for the operation you want.")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
operation = int(input("Enter a number:"))
if 