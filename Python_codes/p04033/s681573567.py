import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
#N = I()
#A = [LI() for _ in range(N)]

a, b = list(map(int,sys.stdin.readline().rstrip().split()))

if a > 0:
    print('Positive')
elif a <= 0 and b >= 0:
    print('Zero')
else:
    if (a+b)%2 == 0:
        print('Negative')
    else:
        print('Positive')