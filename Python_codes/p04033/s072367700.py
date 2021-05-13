def resolve():
    a, b = list(map(int, input().split()))

    if a <= 0 and b >= 0:
        print('Zero')
    elif b < 0 and (b - a + 1) % 2 == 1:
        print('Negative')
    else:
        print('Positive')
    return


resolve()