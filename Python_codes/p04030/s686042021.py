s = input()
n = len(s)

ans = ''

for i in range(n):
    s1 = s[i]
    if s1 == '0':
        ans += '0'
    elif s1 == '1':
        ans += '1'
    else:
        ans = ans[:-1]

print(ans)
