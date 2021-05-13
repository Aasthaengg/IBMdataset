from collections import deque
S = input()
T = deque([])
for s in S:
  if s=="B" and len(T)>0:
    T.pop()
  elif s=="B":
    pass
  else:
    T.append(s)
print("".join(T))