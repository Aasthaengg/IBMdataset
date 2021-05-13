a, b = map(int, input().split())
if a > 0:
  print('Positive')
else:
  if b > 0:
    print('Zero')
  else:
    n = b - a + 1
    if n % 2:
      print('Negative')
    else:
      print('Positive')