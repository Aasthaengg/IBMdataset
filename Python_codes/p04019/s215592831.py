s=list(input())
ss=len(set(s))
if ss==1 or ss==3:
  print('No')
elif ss==4:
  print('Yes')
else:
  if 'N' in s and 'S' in s:
    print('Yes')
  elif 'W' in s and 'E' in s:
    print('Yes')
  else:
    print('No')