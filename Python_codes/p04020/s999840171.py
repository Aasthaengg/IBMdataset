N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
res = 0
p = 0
for a in A:
    if a==0:
        p = 0
    a += p
    res += a//2
    p = a%2
print(res)