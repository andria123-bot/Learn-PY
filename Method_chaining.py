class Car:

  def turn_on(self):
    print("The car has been turned on.")
    return self
  
  def drive(self):
    print("The car is driving.")
    return self
  
  def brake(self):
    print("The car is braking.")
    return self
  
  def turn_off(self):
    print("The car has been turned off.")
    return self

car = Car()

# car.turn_on().drive()
car.brake().turn_off()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()