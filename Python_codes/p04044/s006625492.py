R=list()
N,L=map(int,input().split())
for i in range(N):
  S=input()
  R.append(S)
R=sorted(R)
print("".join(R))