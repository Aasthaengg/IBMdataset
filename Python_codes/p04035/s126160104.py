import sys

read = sys.stdin.read
readline = sys.stdin.readline

N, L, *a = map(int, read().split())
knot = -1
for idx, (i, j) in enumerate(zip(a, a[1:])):
    if i + j >= L:
        knot = idx + 1
        print('Possible')
        break
else:
    print('Impossible')
    exit()

answer = list(range(1, knot)) + list(range(knot + 1, N))[::-1] + [knot]
print('\n'.join(map(str, answer)))
