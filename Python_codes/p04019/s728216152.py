x = list(input())
if 'N' in x and 'S' in x:
  if 'E' in x and 'W' in x:
    print('Yes')
  elif 'E' not in x and 'W' not in x:
    print('Yes')
  else:
    print('No')
elif 'N' not in x and 'S' not in x:
  if 'E' in x and 'W' in x:
    print('Yes')
  elif 'E' not in x and 'W' not in x:
    print('Yes')
  else:
    print('No')
else:
  print('No')