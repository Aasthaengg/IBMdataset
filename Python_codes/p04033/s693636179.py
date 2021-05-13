a,b = map(int,input().split())

if a<=0<=b:
    print('Zero')
else:
    if a<b<0 and (b-a+1)%2!=0:
        print('Negative')
    else:
        print('Positive')