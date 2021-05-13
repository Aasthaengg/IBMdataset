a,b=map(int,input().split())
if 0<a:
  print("Positive")
  exit()
else:
  if b<0:
    S=(b-a+1)%2
    if S==1:
      print("Negative")
    else:
      print("Positive")
  else:
    print("Zero")