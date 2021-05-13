A, B, C = map(int, input().split())

H = [A, B, C]
if H.count(5) == 2 and H.count(7) == 1:
    print('YES')
else:
    print('NO')