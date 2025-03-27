import math as mt
num = int(input("Enter the number:"))

sq = mt.sqrt(num)
log_value = mt.log(num) if num>0 else "Undefined"
sin_val = mt.sin(num)
print(f"Square root: {sq}")
print(f"Logarithm: {log_value}")
print(f"Sine: {sin_val}")
