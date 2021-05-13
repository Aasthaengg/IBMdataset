A,B=map(int,input().split())
if A<=0<=B: print('Zero')
elif 0<A: print('Positive')
else: print('Positive' if (B-A+1)%2==0 else 'Negative')