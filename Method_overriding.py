class Animal:
  def eat(self):
    print("This animal is eating")

class Rabbit(Animal):
  def eat(self):
    print("The rabbit is eating carrots")

rabbit = Rabbit()
rabbit.eat()