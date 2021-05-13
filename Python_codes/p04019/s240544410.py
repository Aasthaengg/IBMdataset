s = list(input())

k, m, n, h = 0, 0, 0, 0

if 'N' in s:
    k = 1
if 'S' in s:
    m = 1
if 'W' in s:
    n = 1
if 'E' in s:
    h = 1

if (abs(k-m))%2 == 0 and (abs(n-h))%2 == 0:
    print('Yes')
else:
    print('No')
