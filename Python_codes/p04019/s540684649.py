# https://atcoder.jp/contests/agc003/tasks/agc003_a

s = input()
d = dict(N=0, W=0, S=0, E=0)

for i in range(len(s)):
    d[s[i]] += 1

if (d['N'] == 0 and d['S'] != 0) or (d['N'] != 0 and d['S'] == 0) or (d['W'] == 0 and d['E'] != 0) or (d['E'] == 0 and d['W'] != 0):
    print('No')
else:
    print('Yes')