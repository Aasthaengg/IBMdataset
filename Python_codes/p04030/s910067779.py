s =input()
ans = []
for i in range(len(s)):
    if (s[i] == '0') or (s[i] == '1'):
        ans.append(s[i])
    elif ans ==[]:
        continue
    else:
        ans.pop()

print(''.join(ans))