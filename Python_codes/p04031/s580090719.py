import numpy as np
input()
A = np.array(input().split(), dtype=np.int32)
print(min((A - i).dot(A - i) for i in range(-100, 101)))