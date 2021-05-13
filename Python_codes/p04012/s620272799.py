S = input()
m = {}

for s in S:
  if s not in m:
    m[s] = 0
  m[s] += 1

for k in m.keys():
  if m[k] % 2 != 0:
    print('No')
    exit()

print('Yes')