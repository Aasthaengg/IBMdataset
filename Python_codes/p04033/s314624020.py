a, b = input().split(' ')
a = int(a)
b = int(b)
if (a<=0 and b>=0) or a==0 or b==0:
  print('Zero')
elif a>0 and b>0:
  print('Positive')
else:
  X = (abs(a) - abs(b))
  if X%2 == 0:
    print('Negative')
  else:
    print('Positive')