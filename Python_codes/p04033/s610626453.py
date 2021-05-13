a,b = map(int, input().split())

if a * b < 0:
    print('Zero')
    exit()
elif a > 0 and b > 0:
    print('Positive')
    exit()
else:
    if abs(a-b) % 2 == 0:
        print('Negative')
    else:
        print('Positive')