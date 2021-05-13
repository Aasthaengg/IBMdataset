n, l = map(int, input().split())
k = [input() for _ in range(n)]
s = sorted(k)
print("".join(s))