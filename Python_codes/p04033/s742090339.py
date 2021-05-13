a, b = list(map(int, input().split()))

if a > 0 and b > 0:
  print("Positive")

elif a < 0 and b < 0:
  if abs(b - a) % 2 == 1:
    print("Positive")

  else:
    print("Negative")

elif a <= 0 and b >= 0:
  print("Zero")