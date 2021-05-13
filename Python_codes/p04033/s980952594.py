# A - Range Product
a,b = map(int,input().split())
if a<=0 and b>=0:
    print('Zero')
elif (max(-a,0)-max(-b-1,0))%2==0:
    print('Positive')
else:
    print('Negative')