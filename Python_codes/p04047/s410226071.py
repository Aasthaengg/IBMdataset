n = int(input())
list_L = list(map(int, input().split()))
list_L.sort()
sum = 0
for i in range(n):
    sum += list_L[2*i]
print(sum)