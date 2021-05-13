a,b=map(int,input().split())
if ( a<0 and b>0 ) or ( a>0 and b<0 ) or a==0 or b==0:
	print('Zero')
else:
	if a>0 and b>0:
		print('Positive')
	else:
		c=b-a
		print('Positive' if c&1 else 'Negative')
