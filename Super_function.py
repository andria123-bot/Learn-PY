class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def area(self):
    return self.length * self.width

class Square(Rectangle):
  def __init__(self, length):
    super().__init__(length, length)

class Cube(Rectangle):
  def __init__(self, length, width, height):
    super().__init__(length, width)
    self.height = height

  def volume(self):
    return self.length * self.width * self.height

square = Square(3)
cube = Cube(3, 3, 3)

print(square.area())
