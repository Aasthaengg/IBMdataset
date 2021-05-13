x,y = map(int,input().split())
if x > 0:
  print("Positive")
elif y<0:
  if((y-x)%2==0):
    print("Negative")
  else:
    print("Positive")
else:
  print("Zero")
