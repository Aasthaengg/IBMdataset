from collections import deque
S = input()
q = deque()

for s in S:
    if s == "B":
        if len(q) != 0:
            q.pop()
    else:
        q.append(s)
print("".join(q))
