a, b = map(int, input().split())

if a>0:
  print("Positive")
elif a*b <= 0:
  print("Zero")
elif abs(b-a)%2:
  print("Positive")
else:
  print("Negative")