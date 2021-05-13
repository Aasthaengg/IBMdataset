s = input()
c = 0
d = 0
if 'W' in s:
  c += 1
if 'E' in s:
  c -= 1
if 'N' in s:
  d += 1
if 'S' in s:
  d -= 1
if c == d == 0:
  print('Yes')
else:
  print('No')