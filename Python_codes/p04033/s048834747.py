import sys
input = sys.stdin.readline

# A - Range Product
a, b = map(int, input().split())

if a > 0:
	print('Positive')
elif b >= 0:
	print('Zero')
else:
	if b > 0:
		b == 0
	
	if (abs(a)-abs(b)+1) % 2 == 1:
		print('Negative')
	else:
		print('Positive')