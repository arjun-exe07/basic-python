#Class Inheritance
class Leapx_org():
  mul_num = 1.2
  def __init__(self,first,last,pay):
    self.first = first 
    self.last = last
    self.pay = pay
    self.fullname = self.first + " " + self.last 

  def make_email(self):
    return self.first + "." + self.last + "@xyz.com" 
  
  def increment(self):
    self.pay = int(self.pay * self.mul_num)
    return self.pay
  
class instructor(Leapx_org):
  def __init__(self,first,last,pay,subject):
    Leapx_org.__init__(self, first,last,pay)
    self.subject = subject


obj1 = instructor("Alice" , "Jenner" , 500000 , "python" )
obj2 = instructor("Jenny" , "Keller" , 600000 , "FDS" )

print(obj1.make_email())
print(obj1.subject)
print(obj2.make_email())
print(obj2.subject)