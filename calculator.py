#!/bin/python3
#Basic Calculator program to take two inputs from user and operation i.e +, - /
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operation = input("Enter an operation (+, -, *): ")

if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "-":
    result = num1 -num2
    print(f"{num1} - {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("You cannot divide a number by 0")
else:
    print("Invalid operation: Try again!")
