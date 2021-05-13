S=input()
a=set()
for s in S:
  a.add(s)
a=list(a)
if len(a)==4:
  print('Yes')
elif len(a)==2:
  if (a[0]=='N' or a[0]=='S') and (a[1]=='N' or a[1]=='S'):
    print('Yes')
  elif (a[0]=='E' or a[0]=='W') and (a[1]=='E' or a[1]=='W'):
    print('Yes')
  else:
    print('No')
else:
  print('No')
