n,l = map(int,input().split())
a = list()
for i in range(n):
     a.append(input())
a.sort()
print(*a,sep="")