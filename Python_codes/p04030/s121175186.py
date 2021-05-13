S = input()
ans = []
for s in S:
    if s == '0' or s == '1':
        ans.append(s)
    else:
        if len(ans) > 0:
            ans.pop(-1)
print(''.join(ans))