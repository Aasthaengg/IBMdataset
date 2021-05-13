import math
import copy

neko = 1
a,b = map(int,input().split())
if (a < 0)and(b < 0):
    if (abs(a-b)+1)%2:
        neko = -1
elif (a<=0)and(0<=b):
    neko = 0
if neko == 1:
    print('Positive')
elif neko == 0:
    print('Zero')
else:
    print('Negative')