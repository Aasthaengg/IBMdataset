a,b=map(int,input().split())
if a <0 and b > 0:
    print('Zero')
    exit()
elif a>0 and b > 0:
    print('Positive')
    exit()
else:
    n = b-a+1
    if n%2 == 0:
        print('Positive')
    else:
        print('Negative')