a = int(input())
b = list(map(int, input().split()))
b.sort()
c = 0
for i in range(len(b)-1, 0, -2):
    c += min(b[i], b[i-1])
print(c)
