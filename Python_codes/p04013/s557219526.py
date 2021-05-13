import sys
from functools import lru_cache

input = sys.stdin.readline


ans = 0
X = []
A = 0

@lru_cache(maxsize=None)
def solve(i, selected, total):
    global X, ans

    if i == len(X):
        if selected != 0 and total == (selected * A):
            return 1
        return 0

    ret = 0
    ret += solve(i + 1, selected + 1, total + X[i])
    ret += solve(i + 1, selected, total)
    return ret


def main():
    global X, ans, A
    N, A = [int(x) for x in input().split()]
    X = [int(x) for x in input().split()]

    print(solve(0, 0, 0))

    
if __name__ == '__main__':
    main()
