class Leapx_org():
  mul_num = 1.20
  def __init__(self , first , last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.full_name = first + " " + last

  def make_email(self):
    return self.first + "." + self.last + "@xyz.com"
  
  def increment(self):
    self.pay = int(self.pay * self.mul_num)
    return self.pay
  
obj1 = Leapx_org("Magnus", "Carlsen" , 60000)
print(obj1.increment())
obj1.mul_num = 1.50
print(obj1.increment())

# print("Instance Space :" , obj1.__dict__ ,end = "\n\n")

# print("Class Space :" , Leapx_org.__dict__)