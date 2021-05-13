a,b=map(int,input().split())
if a<=b<0:
  print('Negative' if (-1)**(a-b-1)==-1 else 'Positive')
elif a<=0<=b:
  print('Zero')
else:
  print('Positive')