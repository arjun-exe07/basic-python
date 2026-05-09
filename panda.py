import pandas as pd

# print(pd.__version__)
'''
  data = [10 , 29 , 65 , 200 , 205, 220]
  s = pd.Series(data , index = ["a" , "b" , "c" , "e" , "f" ,"g"])
'''

employees = {
  "Name" : ["Sanket" , "Arjun" , "Eshwar" ],
  "Age" : [18, 20, 19]
  }

df = pd.DataFrame(employees , index = ["Emp 1" , "Emp 2" , "Emp 3"])
df["Job"] = ["CEO" , None , "Owner"]
print(df)