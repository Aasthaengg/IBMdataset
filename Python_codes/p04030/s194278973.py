s = input()
res = ''
for elem in s:
  if elem == 'B':
    res = res[:-1]
  else:
    res += elem
print(res)