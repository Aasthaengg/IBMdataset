import sys
import os

N, L, *A = map(int, os.read(0, 10**8).split())

def main(L, A):
    N = len(A)
    is_long = [x + y >= L for x, y in zip(A, A[1:])]
    if not any(is_long):
        print('Impossible')
        return
    print('Possible')
    i = is_long.index(True)
    nums = list(range(1, i + 1)) + list(range(N - 1, i, -1))
    print(*nums, sep='\n')

main(L, A)
