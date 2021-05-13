A,B = map(int, input().split())
if A > 0:
  print("Positive")
elif B<0:
  if((B-A)%2 == 0):
    print("Negative")
  else:
    print("Positive")
else:
  print("Zero")