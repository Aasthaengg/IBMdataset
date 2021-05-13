N = int(input())
L = list(map(int, input().split()))
 
L.sort()
s = 0
 
for n in range(N):
    s += L[2*n]
 
print(s)
