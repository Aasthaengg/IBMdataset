N,L = map(int,input().split())
S = sorted([input().strip() for _ in range(N)])
x = ""
for i in range(N):
    x += S[i]
print(x)