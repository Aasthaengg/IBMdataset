a, b = map(int, input().split())

if (a <= 0 and b >= 0):
    print('Zero')
    exit()
elif(a < 0 and b < 0 and a < b):
    c = b - a + 1
    if (c % 2 == 0):
        print('Positive')
    else:
        print('Negative')
else:
    print('Positive')