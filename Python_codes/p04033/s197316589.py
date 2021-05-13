a,b = map(int,input().split())
if a*b < 0 or a*b==0:
    print('Zero')
elif 1<=a :
    print('Positive')
elif b <= -1 and abs(b-a) %2 ==0:
    print('Negative')
else:
    print('Positive')