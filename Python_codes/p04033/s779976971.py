a, b = map(int, open(0).read().split())

if a > 0:
    print('Positive')
elif a == 0 or b == 0:
    print('Zero')
elif a < 0 and b > 0:
    print('Zero')
elif (b-a)%2 == 1:
    print('Positive')
else:
    print('Negative')