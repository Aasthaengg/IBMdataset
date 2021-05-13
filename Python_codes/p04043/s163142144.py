s = [int(x) for x in input().split()]

f5 = 0
f7 = 0
for i in s:
    if 5 == i:
        f5 += 1
    if 7 == i:
        f7 += 1
        
if f5 == 2 and f7 == 1:
    print('YES')
else:
    print('NO')

