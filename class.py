class Leapx_org():
  def __init__(self,first,last,pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.fullname = first + " " + last

  def make_email(self):
    return self.first + "." + self.last + "@xyz.com"

obj1 = Leapx_org("John","Doe",50000)
obj2 = Leapx_org("Jane","Smith",60000)

print(obj1.fullname)
print(obj1.make_email())
print(obj2.fullname)
print(obj2.make_email())
print(Leapx_org.make_email(obj1))