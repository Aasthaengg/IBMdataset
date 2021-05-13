a,b = map(int,input().split())
m = 0
if a<=0 and 0<=b:
    print('Zero')
elif a<0:
    if b < 0:
        m = a-b+1
    else:
        m = abs(a)
    if m%2:
        print('Negative')
    else:
        print('Positive')
else:
    print('Positive')