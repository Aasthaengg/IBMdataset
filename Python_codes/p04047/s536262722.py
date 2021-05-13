import numpy as np
a = input()
c = input().split()

d = [int(i) for i in c]
d.sort()

print(sum(d[0::2]))