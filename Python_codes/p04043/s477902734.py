listA=list(map(int,input().split()))
if listA[0] == 5 and listA[1] == 5 and listA[2] == 7:
    print('YES')
elif listA[0] == 5 and listA[1] == 7 and listA[2] == 5:
    print('YES')
elif listA[0] == 7 and listA[1] == 5 and listA[2] == 5:
    print('YES')
else:
    print('NO')
 