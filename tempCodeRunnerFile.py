from collections import Counter

counter = Counter()

file = open('input.txt', 'r')

for lines in file:
  counter.update(lines.lower().strip())

print(counter)