n,m=map(int,input().split())
if n > 0:
  print('Positive')
elif n * m <= 0:
  print('Zero')
elif (m - n) % 2 == 0:
  print('Negative')
else:
  print('Positive')