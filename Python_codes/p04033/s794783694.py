a,b = map(int,input().split())

if a <= 0 and b >= 0:
	print("Zero")
elif b < 0: 
	print("Positive") if (b - a + 1) % 2 == 0 else print("Negative")
else:
	print("Positive")