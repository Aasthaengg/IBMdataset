A,B=map(int,input().split())
if A<=0 and 0<=B:
    print('Zero')
elif A+B<0 and (A+B)%2==0:
    print('Negative')
else:
    print('Positive')