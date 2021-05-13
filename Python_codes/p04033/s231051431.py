a,b = map(int,input().split())

if a>0 and b>0:
  print("Positive")
  exit()
elif a<=0 and b>=0:
  print("Zero")
  exit()
elif a==0 or b==0:
  print("Zero")
elif a<0 and b<0:
  if (abs(a-b)+1)%2==0:
    print("Positive")
    exit()
  else:
    print("Negative")
    exit()