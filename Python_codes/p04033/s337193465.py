a, b = [int(x) for x in input().split()]
if(a>0):
  print('Positive')
elif(a<=0 and b>=0):
  print('Zero')
else:
  delab = b-a+1
  if(delab%2==0):
    print('Positive')
  else:
    print('Negative')