a, b = map(int, input().split());

if a * b <= 0 : 
  print('Zero')
  exit(0)

if a > 0 and b > 0 :
  print('Positive')
  exit(0)

x = b - a + 1
if(x%2 == 0) : 
  print('Positive')
else :
  print('Negative')

