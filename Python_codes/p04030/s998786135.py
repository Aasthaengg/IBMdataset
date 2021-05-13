s = input()
stack = []
for i in range(len(s)):
    if s[i] == "B":
        if not stack:
            continue
        stack.pop()
    else:
        stack.append(s[i])

print("".join(stack))