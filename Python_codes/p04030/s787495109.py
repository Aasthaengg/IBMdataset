from collections import deque
s=input()

d=deque()
for i in range(len(s)):
    if s[i]=="1":
        d.append("1")
    elif s[i]=="0":
        d.append("0")
    else:
        if len(d)!=0:
            d.pop()

L="".join(d)
print(L)