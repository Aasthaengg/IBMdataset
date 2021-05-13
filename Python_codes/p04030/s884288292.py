s = input()

ans = []
for l in s:
    if l == '0':
        ans.append('0')
    elif l == '1':
        ans.append('1')
    else:
        if ans:
            ans.pop()

print(''.join(ans))