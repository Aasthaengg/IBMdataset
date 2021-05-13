N = int(input())
A = []
a = []
for i in range(N):
    x = int(input())
    if x==0:
        b = a[:]
        A.append(b)
        a = []
    else:
        a.append(x)
A.append(a)
cnt = 0
for a in A:
    c = sum(a)
    cnt += c//2
print(cnt)