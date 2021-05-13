a, b = map(int,input().split())
if a <= 0 and b >= 0:
    print('Zero')
else:
    if a < 0:
        if (min(b+1, 0)-a)%2==0:
            print('Positive')
        else:
            print('Negative')

    else:
        print('Positive')