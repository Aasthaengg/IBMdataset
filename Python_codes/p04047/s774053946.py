n = int(input())
l = [int(x) for x in input().split()]

l.sort()

cnt = 0
for i in range(2*n):
    if i%2 == 0:
        cnt += l[i]
        
print(cnt)