n,L = map(int,input().split())
a = list(map(int,input().split()))

r = [0]
for i in range(n):
    r.append(r[i] + a[i])

ansl = []
p,q = 0,n-1
suma = sum(a)
while p < q:
    if r[q+1] - r[p]  < L:
        print("Impossible")
        exit()
    if a[p] + a[p + 1] <= a[q-1] + a[q]:
        ansl.append(p + 1)
        p+=1
    else:
        ansl.append(q)
        q-=1


print("Possible")
for ans in ansl:
    print(ans)
