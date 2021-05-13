n,m=map(int,input().split())
l=[list(map(int,input().split())) for i in range(m)]

num_l=[1 for i in range(n)]
bit_l=[1]+[0 for i in range(n-1)]

for x,y in l:
  x-=1
  y-=1

  if bit_l[x]==1:
    bit_l[y]=1
    if num_l[x]==1:
      bit_l[x]=0
  num_l[x]-=1
  num_l[y]+=1

print(bit_l.count(1))