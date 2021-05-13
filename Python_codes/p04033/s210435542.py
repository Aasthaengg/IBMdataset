a,b=map(int,input().split())
if a>=1:
    print('Positive')
elif b<=-1:
    if (b-a)%2==0:
        print('Negative')
    else:
        print('Positive')
else:
    print('Zero')