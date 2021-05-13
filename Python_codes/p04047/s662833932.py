import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

L = np.array(read().split(), np.int32)[1:]

L.sort()
x = L[::2].sum()
print(x)