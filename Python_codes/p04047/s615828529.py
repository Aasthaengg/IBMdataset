n = int(input())
li = list(map(int, input().split()))

li.sort()
li1 = []

for i in range(2*n):
    if i%2==0:
        li1.append(li[i])
print(sum(li1))