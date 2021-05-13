import sys

def sum(num) : 
  return int((1 / 2) * num * (num + 1))


for line in sys.stdin : 
  num = int(line)
  

print(sum(num))