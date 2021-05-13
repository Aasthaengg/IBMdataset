from collections import deque
s = input()
lst = deque()
for i in range(len(s)):
  if s[i] == 'B':
    if len(lst) > 0:
      lst.pop()
    else:
      pass
  else:
    lst.append(s[i])
print(''.join(list(lst)))