s=input()
stack =[]
for i in s:
    if i != "B":
        stack.append(i)
    else:
        if not stack:
            continue
        else:
            stack.pop()
print("".join(stack))