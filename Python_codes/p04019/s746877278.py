S=set(x for x in input())
if len(S)==4:
  print('Yes')
elif len(S)==2:
  if 'W' in S and 'E' in S:
    print('Yes')
  elif 'N' in S and 'S' in S:
    print('Yes')
  else:
    print('No')
else:
  print('No')  