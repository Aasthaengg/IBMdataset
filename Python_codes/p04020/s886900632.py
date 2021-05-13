n = int(input())
a = [int(input()) for _ in range(n)]
a.append(0)
r = 0
for i in range(n):
    r += a[i]//2
    if a[i]%2==1 and a[i+1]>0:
        r += 1
        a[i+1] -= 1
print(r)