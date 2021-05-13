n = int(input())
lis = list(map(int,input().split()))
lis.sort()
S = 0
for i in range(n):
    S += lis[2*i]
print(S)
