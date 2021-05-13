a, b = map(int, input().split())

if a <= 0 and b >= 0:
    print('Zero')
if b < 0:
    if (b - a) % 2 == 0:
        print('Negative')
    else:
        print('Positive')
if a > 0:
    print('Positive')