import numpy
a,b = map(int,input().split())

if numpy.sign(a*b)==-1:
  print('Zero')
elif (numpy.sign(a)==1) or (numpy.sign(b)==1):
  print('Positive')
elif (a-b)%2==0:
  print('Negative')
else:
  print('Positive')