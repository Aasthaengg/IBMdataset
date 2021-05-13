N,L=map(int,input().split())
S=[]
for i in range(N):
    S.append(str(input()))
print("".join(sorted(S)))
