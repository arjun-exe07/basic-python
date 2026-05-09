

class NotEligible (Exception):
  pass

try:
  age=int(input("enter your age:"))
  if age<18:
    raise NotEligible("you are not eligible for voting")
  
  else:
    print("you are eligible for voting")

except NotEligible as e:
  print("Custom Error :",e)

