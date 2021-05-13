import numpy as np
import sys

input = sys.stdin.readline

a,b  =  map(int,input().split())


cnt = b - a +1

if a <= 0 and b >= 0:
    print("Zero")
elif a > 0 and b > 0:
    print("Positive")
elif a < 0 and b < 0 and cnt%2 == 0:
    print("Positive")
elif a < 0 and b < 0 and cnt%2 == 1:
    print("Negative")