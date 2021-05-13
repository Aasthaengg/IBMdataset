a,b = map(int, input().split())
if 0 < a and 0 < b:
    print('Positive')
elif a <= 0 <= b:
    print('Zero')
else:
    if (b-a+1)%2 == 1:
        print('Negative')
    else:
        print('Positive')