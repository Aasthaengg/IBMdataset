N, M = map(int, input().split())
L = list(map(int, input().split()))

count = 0
vouch = 0
A = []

for i in range (0, N-1):
	if count == 0:
		if L[i]+L[i+1] >= M:
			count=1
			A.append(N-1)
		else:
			A.append(i+1)
	else:
		A.append(N-2-vouch)
		vouch+=1

if count == 0:
	print('Impossible')
	exit()
else:
	print('Possible')
    
for i in range (0, N-1):
	print(A[i])