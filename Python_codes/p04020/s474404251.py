n = int(input())
ans = 0
lis = [int(input()) for i in range(n)]+[0]

count = 0

for i in range(n):
    if lis[i]%2 == 0:
        count += lis[i]//2
    else:
        if lis[i+1] > 1:
            count += lis[i]//2+1
            lis[i+1] -= 1
        else:
            count += lis[i]//2
print(count)