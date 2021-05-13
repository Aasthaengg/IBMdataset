n=int(input())
li=[int(i) for i in input().split()]

li=sorted(li)
ans=0
for i in range(n):
	ans+=li[i*2]
print(ans)