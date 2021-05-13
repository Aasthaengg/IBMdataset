def resolve():
    a, b = map(int, input().split())
    if 0 in range(a, b+1):
        print('Zero')
    elif a >= 1:
        print('Positive')
    elif b < 0 and len(range(a, b+1)) % 2 == 0:
        print('Positive')
    else:
        print('Negative')

resolve()