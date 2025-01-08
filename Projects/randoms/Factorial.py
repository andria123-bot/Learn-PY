import math
import sys

sys.set_int_max_str_digits(10**6)

num = int(input("Enter a number to calculate its factorial: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = math.factorial(num)
    print(f"The factorial of {num} is: {result}")


