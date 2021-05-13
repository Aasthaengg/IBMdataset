a, b = map(int, input().split())

if a * b < 0:
	print('Zero')
elif a > 0:
	print('Positive')
else:
	diff = b - a
	print('Positive') if diff % 2 != 0 else print('Negative')