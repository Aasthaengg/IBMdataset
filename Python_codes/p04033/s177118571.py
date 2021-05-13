a,b = map(int, input().split())

if (a<0 and 0<b) or a==0 or b==0:
  print("Zero")
  exit()

if a>0:
  print("Positive")
  exit()

if a==b:
  print("Positive")
elif (b-a)%2==1:
  print("Positive")
else:
  print("Negative")

