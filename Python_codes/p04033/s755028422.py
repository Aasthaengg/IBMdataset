import sys
a,b = list(map(int, input().split()))

if a<=0 and b>= 0:
  print("Zero")
  sys.exit()
elif a < 0 and b < 0:
  if (-(a-b)+1)%2 == 0:
    print("Positive")
    sys.exit()
  else:
    print("Negative")
    sys.exit()
elif a==0 or b==0:
  print("Zero")
  sys.exit()
elif a>0 and b>0:
  print("Positive")
  sys.exit()
else:
  if (-a)%2 == 0:
    print("Positive")
  else:
    print("Negative")