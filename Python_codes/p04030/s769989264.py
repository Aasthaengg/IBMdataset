s = input()
ans = ''
for i in s:
    if i != 'B':
        ans = ans + i
    else:
        ans = ans[:-1]
print(ans)