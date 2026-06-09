class circle:
  def __init__(self,radius):
    self.radius = radius

  def area(self):
    return 3.14 * self.radius *self.radius
  
  def perimeter(self):
    return 2* 3.14 *self.radius
  
circ = circle(10)

print(circ.area())
print(f"{circ.perimeter():.2f}")