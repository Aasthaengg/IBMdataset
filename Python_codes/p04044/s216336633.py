n, l = input().split()
n = int(n)
s = [input() for _ in range(n)]
s.sort()
print(*s, sep='')