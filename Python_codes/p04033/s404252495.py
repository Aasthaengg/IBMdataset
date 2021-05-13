A,B=map(int,input().split())
count=0
if A==0 or B==0:
	print("Zero")
	exit()
else:
	if A<0 and B>0:
		print("Zero")
	elif A>0:
		print("Positive")
	elif A<0 and B<0:
		if (abs(B)-abs(A))%2==0:
			print("Negative")
		else:
			print("Positive")