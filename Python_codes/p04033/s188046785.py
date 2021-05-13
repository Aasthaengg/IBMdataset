a,b=map(int,input().split())

if a>0 and b>0:
  print("Positive")
elif a<=0 and b>=0:
  print("Zero")
elif a<0 and b<0:
  if abs(a-b)%2:
    print("Positive")
  else:
    print("Negative")