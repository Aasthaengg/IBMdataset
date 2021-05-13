a, b = map(int, input().split())

if b < 0:
    print('Positive') if (b-a)%2 == 1 else print('Negative')
elif 0 < a:
    print('Positive')
else:
    print('Zero')