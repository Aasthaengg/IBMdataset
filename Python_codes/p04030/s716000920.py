s = input()

ans = []

for i in s:
    if i == '1' or i == '0':
        ans.append(i)
    else:
        if ans == []:
            continue
        else:
            ans.pop()

print(''.join(ans))
