n, l = map(int, input().split())
s = list(input() for _ in range(n))

a = "".join(sorted(s))
print(a)
