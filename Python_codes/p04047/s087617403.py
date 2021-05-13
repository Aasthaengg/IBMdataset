n = int(input())
l = list(map(int, input().split() ))
l.sort()
count = 0
i = 0
while i<len(l):
	count+=l[i]
	i+=2
print(count)