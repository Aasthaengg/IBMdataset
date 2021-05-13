# Begin Header {{{
from math import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement
# }}} End Header
# _________コーディングはここから！！___________
# ... 最小側の制約も確認した？
# ... オーバーフローしない？
s = input()
ans = ""
for x in s:
    if x=='B':
        if ans!="": ans = ans[:-1]
    else: ans+=x
print(ans)