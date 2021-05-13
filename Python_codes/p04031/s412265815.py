import numpy as np
n = int(input())
a = list(map(int, input().split()))
n = len(a)
Mean1 = np.floor(sum(a) / n)
Mean2 = np.ceil(sum(a) / n)
sum1 = sum([(x-Mean1)**2 for x in a])
sum2 = sum([(x-Mean2)**2 for x in a])
print(int(min(sum1, sum2)))
