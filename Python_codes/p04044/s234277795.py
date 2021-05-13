n,l = map(int,input().split())
s = []
for _ in range(n):
	S = str(input())
	s.append(S)

s.sort()
ans = "".join(s)
print(ans)
