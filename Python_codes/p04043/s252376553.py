A,B,C=map(int,input().split())
lst=0
if A==5 or A==7:
    lst+=A
    if B==5 or B==7:
        lst+=B
        if C==5 or C==7:
            lst+=C
            if lst==17:
                print('YES')
            else:
                print('NO')
else:
    print('NO')