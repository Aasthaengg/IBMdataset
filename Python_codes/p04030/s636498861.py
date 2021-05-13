from collections import deque
s = input()
de = deque()
for i in s:
    if i == "0":
        de.append("0")
    elif i == "1":
        de.append("1")
    elif i == "B":
        if len(de) != 0:
            de.pop()
ans = "".join(de)
print(ans)