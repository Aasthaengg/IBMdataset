a,b = map(int,input().split())

if (a>0) & (b>0):
    print('Positive')
elif (a<0) & (b>0):
    print('Zero')
elif (a==0) or(b==0):
    print('Zero')
else:
    if (b-a)%2==1:
        print('Positive')
    else:
        print('Negative')