import cowsay
import sys
from hello import hello

if len(sys.argv) == 2:
  hello(sys.argv[1])

print()

if len(sys.argv) == 2:
  cowsay.cow("Hello " + sys.argv[1])

print()

if len(sys.argv) == 2:
  cowsay.trex("Hello " + sys.argv[1])

