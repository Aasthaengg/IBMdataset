from collections import deque

S=input()
t = deque()

for s in S:
    if s == 'B' and len(t) !=0:
        t.pop()
    elif s == '1' or s == '0':
        t.append(s)
print(''.join(t))
