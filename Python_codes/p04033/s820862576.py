a,b=map(int,input().split())
if a*b<=0:
  print("Zero")
elif a>0 or a==b:
  print("Positive")
else:
  if abs(a-b) % 2 == 0:
    print("Negative")
  else:
    print("Positive")