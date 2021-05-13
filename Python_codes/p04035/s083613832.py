import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, L, *A = map(int, read().split())

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