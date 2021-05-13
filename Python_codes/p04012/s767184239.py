import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

w = input()
import collections
c = collections.Counter(w)
for k, v in c.items():
    if v % 2 != 0:
        print('No')
        quit()
print('Yes')
