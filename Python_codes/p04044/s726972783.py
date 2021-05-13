N,L=map(int,input().split())
X=[]*N
B=0
Ans=""
x=[]*N
s=[]*N
for i in range(N):
    X.append(input())
 
X.sort()

for i in range(N):
    Ans+=(X[i])

print(Ans)