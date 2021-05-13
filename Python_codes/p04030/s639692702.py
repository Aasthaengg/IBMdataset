s = input()

ans = ''

for i in s:
    ans = ans[:-1] if i == 'B' else ans + i    

print(ans)