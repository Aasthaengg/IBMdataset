S = str(input())
import collections

Q = collections.deque()

for i in range (0, len(S)):
	if S[i] == 'B':
		if len(Q) >= 1:
			D = Q.pop()
	else:
		Q.append(S[i])

T = str()
while Q:
	V = Q.popleft()
	T=T+V
    
print(T)