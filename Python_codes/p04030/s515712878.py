from collections import defaultdict
from collections import deque
import itertools
import math

def readInt():
  return int(input())
def readInts():
  return list(map(int, input().split()))
def readChar():
  return input()
def readChars():
  return input().split()

d = deque()

for i in input():
  if i=="0":
    d.append("0")
  elif i=="1":
    d.append("1")
  elif d:
    d.pop()

while d:
  print(d.popleft(),end="")
print()