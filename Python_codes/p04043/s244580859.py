A, B, C = list(map(int, input().split()))
if (A == 7 and B == 5 and C == 5) or (A == 5 and B == 7 and C == 5) or (A == 5 and B == 5 and C == 7):
    print('YES')
else:
    print('NO')