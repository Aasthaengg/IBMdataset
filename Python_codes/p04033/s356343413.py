a,b = map(int,input().split())
if a <= 0 <= b:
    print('Zero')
    exit()
elif a >= 1:
    print('Positive')
elif (abs(b) - abs(a)) % 2 == 0:
    print('Negative')
else:
    print('Positive')