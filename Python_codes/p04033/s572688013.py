x,y = map(int,input().split())

if x <=0 and 0 <= y:
    print('Zero')
elif 0 < x:
    print('Positive')
elif y < 0:
    if (x-y+1)%2==0:
        print('Positive')
    else:
        print('Negative')
