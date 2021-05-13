N, L = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
l, i = max((A[i] + A[i - 1], i) for i in range(1, N))
ans = []
if l >= L:
    print('Possible')
    if i < N - 1:
        ans += list(range(N - 1, i, -1))
        ans += list(range(1, i + 1))
    else:
        ans += list(range(1, i + 1))
    print(*ans, sep='\n')
else:
    print('Impossible')
