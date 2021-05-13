a = int(input())
b = list(map(int, input().split()))
b = sorted(b, reverse=True)
c = 0
for i in range(1, len(b), 2):
    c += min(b[i], b[i-1])
print(c)
