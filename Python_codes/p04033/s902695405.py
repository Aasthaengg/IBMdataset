import sys
import copy
import math
import itertools
import numpy as np
l = [int(c) for c in input().split()]
a = l[0]
b = l[1]
if a*b <= 0:
    print("Zero")
elif a > 0 and b > 0:
    print("Positive")
else:
    if abs(b-a)%2==1:
        print("Positive")
    else:
        print("Negative")
