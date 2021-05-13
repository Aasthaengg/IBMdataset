import sys
N, L = map(int, input().split())
A = [int(_) for _ in input().split()]


for n in range(N - 1):
    if A[n] + A[n + 1] >= L:
        print('Possible')
        tmp_ind = n + 1
        for m in range(1, tmp_ind):
            print(m)
        for m in range(N - 1, tmp_ind, -1):
            print(m)
        print(tmp_ind)
        sys.exit()
print('Impossible')