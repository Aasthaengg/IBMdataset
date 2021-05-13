A, B, C =map(int,input().split())
# B should be 7 and A and C should be 5
if A==7:
    a=A
    b=B
    A=b
    B=a
elif C==7:
    c=C
    b=B
    C=b
    B=c
if A==5 and B==7 and C==5:
    print('YES')
else:
   print('NO')