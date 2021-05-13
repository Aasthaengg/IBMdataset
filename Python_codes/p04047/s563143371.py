n = int(input())
li = list(map(int, input().split()))

l = sorted(li)
lis = []
for i in range(2*n):
    if (i%2 == 0):
        lis.append(l[i])

a = sum(lis)
print(a)