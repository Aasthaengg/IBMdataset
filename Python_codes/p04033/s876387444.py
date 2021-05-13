a, b = map(int, input().split())

if a > b:
    a, b = b, a

if a <= 0 and b >= 0:
    print('Zero')
elif a > 0 and b > 0:
    print('Positive')
else:
    if (- a - b) % 2 == 0:
        print('Negative')
    else:
        print('Positive')
