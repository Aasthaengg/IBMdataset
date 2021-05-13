a,b=map(int,input().split())
if a<=0<=b:
    print('Zero')
elif a<0 and b<0:
    n=abs(a-b)+1
    if n%2==0:
        print('Positive')
    else:
        print('Negative')
else:
    print('Positive')