s = input()

if (
  (('N' in s) and ('S' in s) and (not 'W' in s) and (not 'E' in s)) or
  (('W' in s) and ('E' in s) and (not 'N' in s) and (not 'S' in s)) or
  (('N' in s) and ('S' in s) and ('W' in s) and ('E' in s))
):
  print('Yes')
else:
  print('No')
