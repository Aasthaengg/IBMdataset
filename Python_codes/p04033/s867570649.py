a, b = list(map(int, input().split()))

if a <= 0 and b >= 0:
  print("Zero")
  exit()

if a > 0:
  print("Positive")
  exit()

if (b - a + 1) % 2:
  print("Negative")
else:
  print("Positive")
