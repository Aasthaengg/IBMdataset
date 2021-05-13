n,l = map(int, input().split())
s = []
for _ in range(n):
    s.append(input())
print(*sorted(s), sep='')
