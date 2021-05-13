S = input()

stack = []
for s in S:
    if s == '0' or s == '1':
        stack.append(s)
    if s == 'B':
        if not stack:
            continue
        else:
            stack.pop()

print(''.join(stack))