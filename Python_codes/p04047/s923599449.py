n = int(input())
L = sorted([int(i) for i in input().split()])
count = 0
for i in range(n):
    count += L[i*2]
print(count)