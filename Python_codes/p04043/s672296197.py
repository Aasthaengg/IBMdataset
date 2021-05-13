a = [int(x) for x in input().split()]
countF = 0
countS = 0
for i in range(3):
    countF += a[i] == 5
    countS += a[i] == 7
if countF == 2 and countS == 1:
    print('YES')
else:
    print('NO')