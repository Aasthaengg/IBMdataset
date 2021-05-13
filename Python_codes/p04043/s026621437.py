abc = list(map(int,input().split()))

if abc == [5,5,7]:
    print('YES')
    exit()
if abc == [7,5,5]:
    print('YES')
    exit()
if abc == [5,7,5]:
    print('YES')
    exit()
print('NO')
