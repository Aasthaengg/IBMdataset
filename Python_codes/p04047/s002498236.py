import numpy as np
n = int(input())
l = sorted([int(i) for i in input().split()])
l = np.array(l)
print(np.sum(l[np.arange(0,2*n,2)]))