a,b=map(int,input().split())

if a>0 and b>0:
    print('Positive')
    exit()

elif a<=0 and 0<=b:
    print('Zero')
    exit()
else:
    if abs(b-a)%2==0:
        print('Negative')
        exit()
    else:
        print('Positive')
        exit()