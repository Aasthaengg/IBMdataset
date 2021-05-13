a,b=map(int,input().split())
if a==0 or b==0 or abs(a)==b or (a<0 and b>0):
    print('Zero')
elif a>0 or b>0:
    print('Positive')
else:
    if (abs(a)+abs(b))%2==0:
        print('Negative')
    else:
        print('Positive')

