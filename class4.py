class Leapx_org():
  mul_num = 1.2
  def __init__(self,first,last,pay):
    self.first = first 
    self.last = last
    self.pay = pay
    self.fullname = self.first + " " + self.last 

  def make_email(self):
    return self.first + "." + self.last + "@xyz.com" 
  
  def __add__(self,other):
    result = self.pay + other.pay
    return result
  
obj1 = Leapx_org("John","Doe",50000)
obj2 = Leapx_org("Jane","Smith",60000)

print(obj1 + obj2)
