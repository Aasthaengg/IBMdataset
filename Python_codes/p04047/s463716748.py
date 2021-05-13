n = int(input())
l = list(map(int, input().split()))
l.sort()
sum = 0
#print(l)

for i in range(len(l)):
    if i % 2 == 0:
        sum += l[i]
print(sum)