import numpy as np
import math

n, m = map(int, input().split())
probability = [0 for _ in range(n)]
ball = [1 for _ in range(n)]
probability[0] = 1
for i in range(m):
    x, y = map(int, input().split())
    prob = math.ceil(probability[x-1])
    probability[x-1] = prob * (ball[x-1] - 1) / ball[x-1]
    probability[y-1] += prob / ball[x-1]
    ball[x-1] -= 1
    ball[y-1] += 1
print(np.sum(np.array(probability) > 0))
