# AGC 002: A – Range Product
a, b = [int(s) for s in input().split()]

if a > 0:
    print('Positive')
elif b < 0:
    if (b - a + 1) % 2 == 0:
        print('Positive')
    else:
        print('Negative')
elif a <= 0 <= b:
    print('Zero')