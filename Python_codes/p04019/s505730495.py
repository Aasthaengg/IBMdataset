S = input()
S = list(S)
count = 0
while count == 0:
  if 'N' in S:
    if'S' in S:
      count += 1
    else:
      print('No')
      break
  if 'S' in S:
    if'N' in S:
      count += 1
    else:
      print('No')
      break
  if 'E' in S:
    if'W' in S:
      count += 1
    else:
      print('No')
      break
  if 'W' in S:
    if'E' in S:
      count += 1 
    else:
      print('No')
      break
else:
  print('Yes')