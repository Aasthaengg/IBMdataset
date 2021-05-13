a, b = map(int, input().split())
if a>=0 and b>=0:
    print('Positive')
elif 0>b:
    if (b-a+1)%2==0:print('Positive')
    else:print('Negative')
elif a<=0<=b:
    print('Zero')
else:
    pass