str = input()
ans = list()
for s in str:
    if s == 'B':
        if ans:
            ans.pop()
        continue
    else:
        ans.append(s)
print("".join(ans))