a, b = list(map(int, input().split()))

if a*b <= 0:
  print("Zero")
elif a > 0:
  print("Positive")
elif b < 0 and (-a-b)%2 == 1:
  print("Positive")
else:
  print("Negative")