class organism:
  alive = True

class Animal(organism):

  def eat(self):
    print("Eating...")

class Cat(Animal):

  def meow(self):
    print("Meow!")

cat = Cat()

