N,L=map(int,input().split())
inp=[]
for i in range(N):
    inp.append(input())

inp.sort()
ans=""
for i in range(N):
    ans+=inp[i]
print(ans)