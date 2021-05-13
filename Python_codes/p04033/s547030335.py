a,b = map(int,input().split())

if a <= 0 and b >= 0:
    print('Zero')
    exit()

if a > 0 and b > 0:
    print('Positive')
    exit()

d = b - a
if d % 2 == 0:
    print('Negative')
else:
    print('Positive')


