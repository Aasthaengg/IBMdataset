a,b = map(int, input().split())

if a*b <= 0:
    print('Zero')
elif a>0:
    print('Positive')
elif (abs(a-b)+1)%2 == 0:
    print('Positive')
else:
    print('Negative')