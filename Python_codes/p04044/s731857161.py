N,L = map(int, input().split())
S = [input() for l in range(N)]

S.sort()

s1 = S[0]

for i in range(1,N):
  s1 += S[i]
  
print(s1)