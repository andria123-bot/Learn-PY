class Prey:
  def flee(self):
    print("This is flees")

class Predator:
  def hunt(self):
    print("This animal is hunting")

class Rabbit(Prey):
  pass

class Hawk(Predator):
  pass

class Fish(Prey, Predator):
  pass

Rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

# rabbit.flee()
# hawk.hunt()

fish.flee()

fish.hunt()