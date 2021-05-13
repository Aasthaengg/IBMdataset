a,b=map(int,input().split())
if a>0:
	print('Positive')
elif a*b<=0:
	print('Zero')
else:
	print('Negative' if (b-a+1)%2 else 'Positive')