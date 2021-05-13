N,M= list(map(int,input().split()))
dot=[1]*N
sw=[0] * N
sw[0]=1
for i in range(M):
   a,b=list(map(int,input().split()))
   a-=1;b-=1
   dot[a]-=1
   dot[b]+=1
   if sw[a]:
      sw[b]=1
   if dot[a] == 0:
      sw[a]=0
print(sw.count(1))