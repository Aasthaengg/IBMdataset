s = input()

l = []
for i in s:
  if i != "B":
    l.append(i)
  else:
    if l != []:
      l.pop(-1)

print(''.join(l))
