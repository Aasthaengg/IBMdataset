a, b = map(int, input().split())
if (a <= 0 and b >= 0) or (a >= 0 and b <= 0):
  print("Zero")
elif a > 0:
  print("Positive")
elif b < 0:
  print("Negative") if (abs(b-a)+1) % 2 == 1 else print("Positive")