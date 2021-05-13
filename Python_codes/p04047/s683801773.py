n = int(input())
l = list(map(int,input().split()))
l.sort()

a = []

for i in range(2*n):
    if i % 2 == 0:
        a.append(l[i])

#print(a)
print(sum(a))
