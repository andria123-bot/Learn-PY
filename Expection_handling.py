try:
  numerator = int(input("Enter a number to divide: "))
  denominator = int(input("Enter a number to divide by: "))
  resoult = numerator / denominator
  print(resoult)

except ZeroDivisionError as e:
  print("Error: Division by zero is not allowed.")
  print("Detail:", e)

except ValueError as e:
  print("Error: Invalid input. Please enter a valid number.(")
  print("Detail:", e)

# except Exception as e:
#   print("Something went wrong: (")
#   print("Detail:", e)
else:
  print(resoult)
finally:
  print("This code block will always run.")
