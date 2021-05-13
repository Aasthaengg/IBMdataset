n = int(input())
ls = sorted(list(map(int, input().split())))
total = 0
for i in range(n):
    total += min(ls[2*i], ls[2*i+1])
print(total)