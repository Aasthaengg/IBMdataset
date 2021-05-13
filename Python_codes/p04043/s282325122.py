a = list(map(int,input().split()))
b = a.count(5)
c = a.count(7)

if b == 2 and c == 1:
    print('YES')
else:
    print('NO')