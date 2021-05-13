w = input()

for x in w:
  if w.count(x) % 2 == 0:
    w.replace(x, '')
  else:
    print('No')
    exit()
print('Yes')