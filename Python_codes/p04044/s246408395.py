N,L=map(int,input().split())
S=[]
for i in range(N):
    S.append(input())
S.sort()
Ans=S[0]
for i in range(1,N):
    Ans+=S[i]
print(Ans)