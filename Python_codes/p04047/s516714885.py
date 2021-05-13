n = int(input())
l = list(map(int,input().split()))
list.sort(l)
count = 0

for i in range(0,n*2,2):
    count = count + l[i]

print(count)