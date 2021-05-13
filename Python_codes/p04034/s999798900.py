(n, m), *q = [[*map(int, i.split())] for i in open(0)]
b = [0] * (n + 1)
b[1] = 1
c = [1] * (n + 1)
for x, y in q:
    c[x] -= 1
    c[y] += 1
    b[y] |= b[x]
    b[x] *= c[x] > 0
print(sum(b))
