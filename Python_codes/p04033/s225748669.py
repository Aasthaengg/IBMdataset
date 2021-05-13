a, b = map(int, input().split())
n = 1
L = []
if a * b < 0:
  print('Zero')
elif a + b > 0 or (a - b) % 2 == 1:
  print('Positive')
else:
  print('Negative')