S = input()
stack = []
for c in S:
    if c == '0' or c == '1':
        stack.append(c)
    elif len(stack) > 0:
        stack.pop()
print("".join(stack))