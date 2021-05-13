from collections import deque
s=input()
n=len(s)
stack=deque([])
for i in range(n):
    if s[i]=="0":
        stack.append("0")
    elif s[i]=="1":
        stack.append("1")
    else:
        if stack:
            x=stack.pop()
stack=list(stack)
print("".join(stack))