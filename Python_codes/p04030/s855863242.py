s = input()
ans = []
for i in range(len(s)):
    if s[i] == '0':
        ans.append(0)
    elif s[i] == '1':
        ans.append(1)
    else:
        if ans != []:
            ans.pop()
print(''.join(str(n) for n in ans))