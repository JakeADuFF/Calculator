def add():
    num1 = int(input("Give me your first number: "))
    num2 = int(input("Give me your second number: "))
    print(num1, "+", num2, "=", num1 + num2)

def subtract():
    num3 = int(input("Give me your first number: "))
    num4 = int(input("Give me your second number: "))
    print(num3, "-", num4, "=", num3 - num4)

def division():
    num5 = int(input("Give me your first number: "))
    num6 = int(input("Give me your second number: "))
    print(num5, "÷", num6, "=", num5 / num6)

def multiplication():
    num7 = int(input("Give me your first number: "))
    num8 = int(input("Give me your second number: "))
    print(num7, "x", num8, "=", num7 * num8)

import time
import sys

def gradual_print(text, delay=0.07):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(" ")

def main():
    gradual_print("Welcome to calculator!")
    gradual_print("What would you like to do ?")
    gradual_print("1.add")
    gradual_print("2.subtract")
    gradual_print("3.division")
    gradual_print("4.multiplication")
    choice = int(input(">"))
    
    if choice == 1:
        add()
    elif choice == 2:
        subtract()
    elif choice == 3:
        division()
    elif choice == 4:
        multiplication()
    else:
        print("I can't do that")

main()
