N,L = map(int,input().split())
S = sorted([input().strip() for _ in range(N)])
print("".join(S))