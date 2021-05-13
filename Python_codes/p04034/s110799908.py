n, m = map(int, input().split())
XY = list(map(int, input().split()) for _ in range(m))

Ball = [1] * n
Done = [False] * n
Done[0] = True

for i in range(m):
	x, y = XY[i]
	x -= 1
	y -= 1
	if Done[x]:
		Done[y] = True
	
	Ball[x] -= 1
	Ball[y] += 1
	
	if Ball[x] == 0:
		Done[x] = False
				
res = 0
for i in range(n):
	if Done[i]:
		res += 1

print(res)
