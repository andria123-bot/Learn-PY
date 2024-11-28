class Animal:
  alive = True

  def eat(self):
    print('Eating...')
  
  def sleep(self):
    print('Sleeping...')
  
class Rabbit(Animal):
  def run(self):
    print('Running...')

class Fish(Animal):
  def swim(self):
    print('Swimming...')

class Hawk(Animal):
  def fly(self):
    print('Flying...')

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.slumber()

rabbit.run()
fish.swim()
hawk.fly()

