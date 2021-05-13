a, b = map(int,input().split())
a = min(a,b)
b = max(a,b)
if a != abs(a):
  if b == abs(b): print("Zero")
  elif (b - a) % 2 == 0: print("Negative")
  else: print("Positive")
elif a == 0: print("Zero")
else: print("Positive")  