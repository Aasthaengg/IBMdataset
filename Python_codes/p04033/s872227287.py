a, b = [int(x) for x in input().strip().split()]
if a <= 0 and 0 <= b:
  print('Zero')
elif a > 0:
  print('Positive')
else:
  if (b - a) % 2:
    print('Positive')
  else:
    print('Negative')