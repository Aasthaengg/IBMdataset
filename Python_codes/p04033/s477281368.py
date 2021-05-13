a, b = map(int, input().split())
if a <= 0 <= b:
    print('Zero')
    exit()

if a > 0:
    print('Positive')
else:
    if (abs(a) - abs(b) + 1) % 2 == 0:
        print('Positive')
    else:
        print('Negative')
