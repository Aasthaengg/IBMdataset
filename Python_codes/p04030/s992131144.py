li = list(input())
ans = []
for i in range(len(li)):
    if (li[i] == '0') or (li[i] == '1'):
        ans.append(li[i])
    elif len(ans) > 0:
        ans.pop()
    else:
        pass

print(''.join(ans))