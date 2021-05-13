a,b = map(int,input().split())

if a > 0:
  print("Positive")
  exit(0)
  
if (a == 0 or b == 0) or (a < 0 and b > 0):
  print("Zero")
  exit(0)
  
# only negative a,b cases left from this point on
if (a == b):
  print("Negative")
  exit(0)
  
if (a - b) % 2 == 1:
  print("Positive")
else:
  print("Negative")
