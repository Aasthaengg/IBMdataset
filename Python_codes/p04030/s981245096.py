from collections import deque

S = input()
d = deque()

for s in S:
    if s == 'B':
        if len(d) > 0:
            d.pop()
    else:
        d.append(s)
print("".join(map(str, d)))
