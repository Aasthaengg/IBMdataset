# https://atcoder.jp/contests/agc003/tasks/agc003_b
# 各数字について、その数字の１つ前とその数字だけでできるだけ作る。
# その数字だけでペアをできるだけ作る。
# 1については、0のカードが0枚なので、実質無視できる。
from collections import defaultdict
n = int(input())
d = defaultdict(int)
for i in range(n):
    num = int(input())
    d[i + 1] = num

ans = 0
for i in range(1, n + 1):
    pre = d.get(i - 1, 0)
    cur = d.get(i, 0)
    t = min(pre, cur)
    ans += t
    d[i - 1] -= t
    d[i] -= t
    cur = d.get(i, 0)
    t = cur // 2
    ans += t
    d[i] -= t * 2
print(ans)