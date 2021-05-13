a,b = map(int,input().split())
if b<0:
	print("Positive" if (b-a)%2 else "Negative")
elif a>0:
	print("Positive")
else:
	print("Zero")