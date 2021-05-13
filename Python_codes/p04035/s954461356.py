import sys

N, L = map(int, input().split())
a = list(map(int, input().split()))

for i in range(N-1):
    if(a[i]+a[i+1] >= L):
        idx = i
        break
else:
    print("Impossible")
    sys.exit()
    
print("Possible")

for i in range(1, i+1):
    print(i)
    
for i in range(N-1, i, -1):
    print(i)