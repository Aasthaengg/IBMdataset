a, b = map(int, input().split(' '))
result = 'Positive'
if a <= 0 <= b:
	result = 'Zero'
elif b < 0 and (b - a) % 2 == 0:
	result = 'Negative'
print(result)