import sys
a,b=map(int,input().split())
if a>=0:
  print("Positive")
  sys.exit()
if b>=0:
  print("Zero")
  sys.exit()
if abs(a-b)%2==0:
  print("Negative")
else:
  print("Positive")