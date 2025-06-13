# Python Assignments

This repository contains multiple Python assignments, each consisting of two tasks.

---

## Assignment 1
This assignment includes two tasks:  
- `Assignment1task1.py`
- `Assignment1task2.py`

### **Task 1: Basic Arithmetic Operations**
This script takes two numbers as input and performs basic arithmetic operations.  
```python
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
```

### **Task 2: Greeting with First and Last Name**
This script takes the first and last name as input and prints a welcome message.  
```python
a = input("Enter your first name: ")
b = input("Enter your last name: ")

print("Hello,", a, b, "! Welcome to the Python program.")
```

---

## Assignment 2
This assignment includes two tasks:  
- `Assignment2task1.py`
- `Assignment2task2.py`

### **Task 1: Even or Odd Number Checker**
This script checks whether a given number is even or odd.  
```python
a = int(input("Enter a number: "))

if a % 2 == 0:
    print(a, "is an Even number.")
else:
    print(a, "is an Odd number.")
```

### **Task 2: Sum of Numbers from 1 to 50**
This script calculates the sum of numbers from 1 to 50 using a while loop.  
```python
i = 1
count = 0

while i <= 50:
    count += i
    i += 1

print("The sum of numbers from 1 to 50 is:", count)
```

---

## Assignment 3
This assignment includes two tasks:  
- `Assignment3task1.py`
- `Assignment3task2.py`

### **Task 1: Factorial Calculation**
This script calculates the factorial of a given number using recursion.  
```python
def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)

num = int(input("Enter a number: "))
fact = factorial(num)
print(f"Factorial of {num} is: {fact}")
```

### **Task 2: Mathematical Calculations**
This script performs three mathematical operations:  
- Square root
- Natural logarithm (log base e)
- Sine of the number (in radians)

```python
import math

num = float(input("Enter a number: "))

sq = math.sqrt(num)
log_value = math.log(num) if num > 0 else "Undefined (logarithm of non-positive numbers is not defined)"
sin_val = math.sin(num)

print(f"Square root: {sq}")
print(f"Natural Logarithm: {log_value}")
print(f"Sine: {sin_val}")
```

---

# Assignment 4  
This assignment includes two tasks:  
- `Assignment4task1.py`  
- `Assignment4task2.py`

---

### **Task 1: Read a File and Handle Errors**  
This script opens and reads a file named `sample.txt`. It prints the file's content line by line and handles the error gracefully if the file does not exist.

```python
# Assignment4task1.py

try:
    with open("sample.txt", "r") as file:
        print("File content:\n")
        for line in file:
            print(line.strip())  # strip() removes leading/trailing whitespace, including newlines
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")



## How to Run the Scripts
1. Clone this repository:
   ```sh
   git clone https://github.com/YOUR_USERNAME/Python-Assignments.git
   ```
2. Navigate to the repository:
   ```sh
   cd Python-Assignments
   ```
3. Run any script using Python:
   ```sh
   python Assignment1task1.py
   python Assignment1task2.py
   python Assignment2task1.py
   python Assignment2task2.py
   python Assignment3task1.py
   python Assignment3task2.py
   ```

---

