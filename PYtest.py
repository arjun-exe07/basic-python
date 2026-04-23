from hello import sq
#checking pytest lib

def test_sq():
  #AssertionError
  assert sq(2) == 4
  assert sq(3) == 9
  assert sq(-2) == 4
  assert sq(-3) == 9
  assert sq(0) == 0

#pytest name.py 
#to run the module