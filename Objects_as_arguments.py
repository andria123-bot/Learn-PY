class Car:
  color = None

class Motorcycle:
  color = None

def change_color(car, color):
  car.color = color

car1 = Car()
car2 = Car()
car3 = Car()

bike1 = Motorcycle()

change_color(car1, "red")
change_color(car2, "blue")
change_color(car3, "green")
change_color(bike1, "black")

print(car1.color)  # Output: red
print(car2.color)  # Output: blue
print(car3.color)  # Output: green
print(bike1.color) # Output: black