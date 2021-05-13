a, b = map(int, input().split())

if a <= 0 <= b:
    print('Zero')
elif 0 < a <= b or not (b - a + 1) % 2:
    print('Positive')
else:
    print('Negative')