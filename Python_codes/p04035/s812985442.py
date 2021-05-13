N, L = map(int, input().split())
a = list(map(int, input().split()))
S = sum(a)

t = 0
m = 0
for k in range(len(a)-1):
    if a[k]+a[k+1]>=L:
        t = 1
        m = k+1
        break
if t == 0:
    print("Impossible")
    exit()
else:
    print("Possible")
    for k in range(1,m):
        print(k)
    for l in range(len(a)-(k+2)):
        print(len(a)-l-1)
    print(m)