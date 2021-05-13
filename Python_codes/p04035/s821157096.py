import sys

def solve():
    input = sys.stdin.readline
    N, L = map(int, input().split())
    A = [int(a) for a in input().split()]
    for i in range(N - 1):
        if A[i] + A[i+1] >= L:
            print("Possible")
            for k in range(i): print(k + 1)
            for k in reversed(range(i + 1, N - 1)): print(k + 1)
            print(i + 1)
            break
    else: print("Impossible")

    return 0

if __name__ == "__main__":
    solve()