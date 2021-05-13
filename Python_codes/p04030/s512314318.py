#33 B - バイナリハックイージー
from collections import deque
S = input()

ans = deque([])
for s in S:
    if s == 'B' and len(ans) >= 1:
        ans.pop()
    elif s == '0' or s == '1':
        ans.append(s)
print(''.join(ans))  