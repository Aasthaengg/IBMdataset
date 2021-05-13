S = input()
s_set = set()
for s in S:
  s_set.add(s)
if len(s_set) == 4:
  print('Yes')
elif len(s_set) == 2 and (('W' in s_set and 'E' in s_set) or \
('S' in s_set and 'N' in s_set)):
  print('Yes')
else:
  print('No')
