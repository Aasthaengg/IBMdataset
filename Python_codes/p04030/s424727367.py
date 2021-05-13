com = list(input())
ans = []
for c in com:
    if c == '0':
        ans.append("0")
    elif c == '1':
        ans.append("1")
    elif c == 'B':
        if len(ans) == 0:
            pass
        else:
            ans.pop()
a = "".join(ans)
print(a)