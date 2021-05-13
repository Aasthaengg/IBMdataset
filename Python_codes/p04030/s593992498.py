S = input()
Ans = []
for s in S:
    if not s=='B':
        Ans.append(s)
        continue
    if not Ans:
        continue
    Ans = Ans[:-1]

print(''.join(Ans))
