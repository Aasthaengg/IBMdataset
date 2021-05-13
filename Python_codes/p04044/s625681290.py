n, l = map(int, input().split())
ss = [input() for i in range(n)]
ss = sorted(ss)

for s in ss:
    print(s, end="")
print()
