s = str(input())
ans = ''
for key in s:
    if '0' == key:
        ans += '0'
    elif '1' == key:
        ans += '1'
    else:
        if len(ans) != 0:
            ans = ans[:-1]
print(ans)
