n = int(input())
l = list(map(int,input().split()))
l.sort()
skewers = 0
for i in range(0,2*n,2) :
  skewers += l[i]

print(skewers)