N = int(input())
cards = 0
pairs = 0
for _ in range(N):
	A = int(input())
	if A:
		cards += A
	else:
		pairs += cards//2
		cards = 0
pairs += cards//2
print(pairs)