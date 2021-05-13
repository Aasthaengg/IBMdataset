#!/usr/bin/env python3
(n, m), *q = [[*map(int, i.split())] for i in open(0)]
b = [1] + [0] * (n - 1)
c = [1] * n
for x, y in q:
    c[x - 1] -= 1
    c[y - 1] += 1
    b[y - 1] |= b[x - 1]
    b[x - 1] *= c[x - 1] > 0
print(sum(b))
