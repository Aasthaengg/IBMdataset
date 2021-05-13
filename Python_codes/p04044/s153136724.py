N, L = map(int, input().split())
S = []
for i in range(N):
    S.append(input())

S.sort()
for X in S:
    print(X, end="")
 

