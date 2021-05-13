li = list(map(str, input()))
x=0
y=0

if 'N' in li and 'S' in li and not 'E' in li and not 'W' in li:
  print('Yes')
  exit()
  
if 'E' in li and 'W' in li and not 'S' in li and not 'N' in li:
  print('Yes')
  exit()

for i in range(len(li)):
  if li[i]=='N':
    x=x+1
  elif li[i]=='S':
    x=x-1
  elif li[i]=='E':
    y=y+1
  elif li[i]=='W':
    y=y-1

if x==0 and y==0:
  print('Yes')
else:
  print('No')