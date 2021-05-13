N = int(input())
A = list(map(int, input().split()))
C = 10 ** 9
for i in range(-100, 101):
    c = 0
    for a in A:
        c += (i - a) ** 2
    C = min(C, c)
print(C)