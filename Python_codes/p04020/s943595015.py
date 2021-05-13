N = int(input())
A = int(input())
ans = A//2
amari = A % 2
for _ in range(N-1):
    A = int(input())
    ans += (amari+A)//2
    if A == 0:
        amari = 0
    else:
        amari = (amari+A) % 2
print(ans)
