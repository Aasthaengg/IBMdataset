input_str = list(input())
ans = ''
for i in input_str:
    if i == '0':
        ans = ans +'0'
    elif i == '1':
        ans = ans + '1'
    elif i == 'B':
        if ans == None:
            continue
        else:
            ans = ans[:-1]
print(ans)