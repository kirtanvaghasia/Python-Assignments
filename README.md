# Python-Assignments

## Assignment 1
- Assignment1task1.py and Assignment1tas2 are the two task of Assignment 1.
- ### Task1
- a= int(input("Enter the first number:"))
- b= int(input("Enter the second number:"))
- print("Addition:",(a+b))
- print("Substraction",(a-b))
- print("Multiplication",(a*b))
- print("Division",(a/b))

- ### Task1
- a= input("Enter the first name:")
- b= input("Enter the last name:")
- print("Hello,",a,"",b,"! Welcome to the Python program.")

## Assignment 2
- Assignment2task1.py and Assignment2tas2 are the two task of Assignment 2.

- ### Task1
- a= int(input("Enter a number:"))

- if a%2 == 0:
-     print(a," is Even nunber.")
- else:
-     print(a," is odd number")

- ### Task2
- i=0
- count=0
- while(i<=50):
-     count += i
-    i += 1 

- print("the sum of number from 1 to 50 is :",count)

## Assignment 3
- Assignment3task1.py and Assignment3tas2 are the two task of Assignment 3.

- ### Task 1
- def factorial(number):
-     if number == 0 or number == 1:
-         return 1
-     return number * factorial(number-1)


- num = int(input("Enter the number:"))
- fact = factorial(num)
- print(f"factorial of {num} is: {fact}")


- ### Task 2
- import math as mt
- num = int(input("Enter the number:"))

- sq = mt.sqrt(num)
- log_value = mt.log(num) if num>0 else "Undefined"
- sin_val = mt.sin(num)
- print(f"Square root: {sq}")
- print(f"Logarithm: {log_value}")
- print(f"Sine: {sin_val}")
