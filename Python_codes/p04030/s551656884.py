s = input()

ans  = ''

for x in s:
    if x == 'B':
        if ans == '':
            continue 
        ans = ans[:-1]
    else:
        ans += x

print(ans)
