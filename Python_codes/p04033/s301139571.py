a,b = list(map(int, input().split()))
if a <= 0 <= b:
    print('Zero')
elif a <= b < 0 and (b-a) % 2 == 0:
    print('Negative')
else:
    print('Positive')
