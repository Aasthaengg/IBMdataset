abc = list(map(int, input().split()))
abc.sort()
if abc[0] == abc[1] == 5:
    if abc[2] == 7:
        print('YES')
    else:
        print('NO')
else:
    print('NO')