data=list(input().split())
a=0
b=0
for i in range(0,3):
    if data[i]=='5':
        a=a+1
    elif data[i]=='7':
        b=b+1
if (a==2 and b==1):
    print('YES')
else:
    print('NO')