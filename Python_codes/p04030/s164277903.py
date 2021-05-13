s = input()
stack = []

for i in s:
  if i == 'B' and stack:
    stack.pop()
  elif i != 'B':
    stack.append(i)
print(''.join(stack))