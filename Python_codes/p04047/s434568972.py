N = int(input())
L = list(map(int,input().split()))
L.sort()
out = 0
for i in range(N):
    out += L[2*i]
print(out)