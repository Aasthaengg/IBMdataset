n = int(input())
l = sorted(list(map(int, input().split())), reverse=True)
t = 0
for i in range(1, n * 2, 2):
    t += min(l[i], l[i-1])
print(t)
