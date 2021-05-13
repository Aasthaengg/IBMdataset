S = input()
ans = ''
for s in S:
    if s == '0' or s == '1':
        ans += s
    else:
        if len(ans) > 0:
            ans = ans[:-1]
print(ans)