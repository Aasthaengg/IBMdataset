from sys import stdin
from itertools import groupby
n = int(stdin.readline().rstrip())
li = [int(stdin.readline().rstrip()) for _ in range(n)]
count = 0
point = 0
for i in li:
    if i == 0:
        point += count//2
        count = 0
    else:
        count += i
point += count//2
print(point)