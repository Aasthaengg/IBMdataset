a,b = map(int,input().split())

if a * b <= 0:
  print("Zero")
else:
  if a > 0:
    print("Positive")
  else:
    cnt = b - a + 1
    
    if cnt % 2 == 0:
      print("Positive")
    else:
      print("Negative")

