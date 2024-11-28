class Duck:
  def walk(self):
    print("The duck is walking")
  
  def talk(self):
    print("The duck is quacking")

class Chicken:
  def waken(self):
    print("The chicken is waking up")
  
  def talk(self):
    print("The chicken is clucking")

class Person():
  def catch(self, duck):
    duck.walk()
    duck.talk()
    print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)