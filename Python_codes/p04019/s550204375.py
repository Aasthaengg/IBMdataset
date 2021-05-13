S = input()
count =0
if 'S' in S:
  if 'N' not in S:
    count = 1
if 'N' in S:
  if 'S' not in S:
    count = 1
if 'W' in S:
  if 'E' not in S:
    count = 1
if 'E' in S:
  if 'W' not in S:
    count = 1
if count ==1:
  print('No')
else:
  print('Yes')