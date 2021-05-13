s = input()
ans = []

for c in s:
    if c == '0':
        ans.append('0')
    elif c == '1':
        ans.append('1')
    else:
        if ans:
            ans.pop()
        else:
            continue

print(''.join(ans))
