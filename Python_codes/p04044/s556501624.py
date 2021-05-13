N, L = map(int, input().split())
s = []

for _ in range(N):
	s.append(input())

s.sort()
print(''.join(s))