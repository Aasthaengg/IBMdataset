from collections import deque
S = input()
L = len(S)
d = deque()
for i in range(L):
    if S[i] == "0":
        d.append("0")
    elif S[i] == "1":
        d.append("1")
    else:
        if len(d) != 0:
            d.pop()

ans = ''.join(d)
print(ans)
