a,b=map(int, input().split())
ans=1
if a <= 0 and b >= 0:
  print('Zero')
  exit(0)
if a>0 and b > 0:
  print('Positive')
  exit(0)
if a <0 and b<0:
  d=abs(b-a)+1
  if d %2==0:
    print('Positive')
    exit(0)
  else:
    print('Negative')
    exit(0)