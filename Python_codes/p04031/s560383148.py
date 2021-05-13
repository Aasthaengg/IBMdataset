import numpy as np
n = int(input())
xs = [int(x) for x in input().split()]
a = int(np.average(xs))
b = a + 1
print(min(sum([(x - a) ** 2 for x in xs]), sum([(x - b) ** 2 for x in xs])))
