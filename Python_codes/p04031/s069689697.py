N=int(input())
S=list(map(int,input().split()))
D=[]
for i in range(-101,102):
    goukei=0
    for j in range(N):
        goukei+=(S[j]-i)**2
    D.append(goukei)

print(min(D))