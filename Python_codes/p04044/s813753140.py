N,L=map(int,input().split())
S=list()
for i in range(N):
    S.append(input())
S.sort()
for i in range(N):
    print(S[i],end="")
print()