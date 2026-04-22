import sys
if len(sys.argv) < 2:
  sys.exit("Too few arguments.")

for arg in sys.argv[1:]:
  print(f"Hello , {arg}")

try:
  print(f"hello , {sys.argv[1]}")
except IndexError:
  print(f"too few arguments.")