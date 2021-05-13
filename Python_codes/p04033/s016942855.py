a, b = list(map(int, input().split()))
p = 1

if 0 < a and 0 < b:
    print('Positive')
elif a <= 0 and 0 <= b or 0 <= a and b <= 0:
    print('Zero')
else:
    if (b - a + 1) % 2 == 0:
        print('Positive')
    else:
        print('Negative')