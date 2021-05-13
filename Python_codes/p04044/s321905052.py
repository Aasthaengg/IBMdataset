N,L=map(int,input().split())
ans=""
S=[]
for i in range(N):
    S.append(str(input()))

S=sorted(S)
for j in range(N):
    ans+=S[j]
print(ans)