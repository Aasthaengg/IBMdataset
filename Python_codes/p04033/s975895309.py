a, b = map(int, input().split())
if a < 0 and b < 0:
    if (max(a, b) - min(a, b) + 1) % 2:
        print('Negative')
    else:
        print('Positive')
else:
    if a * b <= 0:
        print("Zero")
    else:
        print('Positive')
