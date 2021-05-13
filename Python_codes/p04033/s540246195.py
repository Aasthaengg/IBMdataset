a, b = map(int, input().split())
if a*b<0:
    print('Zero')
elif a>0 or (b-a)%2:
    print('Positive')
else:
    print('Negative')