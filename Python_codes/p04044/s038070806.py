INP=list(map(int, input().split()))
N,L=INP[0],INP[1]
Slist=[]
for i in range(N):
  Slist.append(str(input()))
print("".join(sorted(Slist)))