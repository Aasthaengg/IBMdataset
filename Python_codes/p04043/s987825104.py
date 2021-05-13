ans = []
A, B, C = map(int, input().split())
ans.append(A)
ans.append(B)
ans.append(C)
if ans.count(5) == 2 and ans.count(7) == 1:
    print('YES')
else:
    print('NO')
