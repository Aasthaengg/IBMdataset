A, B = map(int, input().split())
if A <= 0 and B >= 0:
  print('Zero')
elif A > 0 and B > 0:
  print('Positive')
else:
  if (B-A)%2 != 0:
    print('Positive')
  else:
    print('Negative')