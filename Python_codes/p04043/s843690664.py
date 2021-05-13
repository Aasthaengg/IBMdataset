a,b,c = (int(x) for x in input().split())

if a==7 and b==5 and c==5:
    print('YES')
elif a==5 and b==7 and c==5:
    print('YES')
elif a==5 and b==5 and c==7:
    print('YES')
else:
    print('NO')