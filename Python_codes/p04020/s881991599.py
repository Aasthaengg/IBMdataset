import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    A = list(int(readline()) for _ in range(N))

    ans = 0
    for i in range(N):
        if i==N-1:
            ans += A[i] // 2
        else:
            ans += A[i]//2
            A[i] %= 2
            if A[i]==1 and A[i+1]>0:
                ans += 1
                A[i] = 0
                A[i+1] -= 1
    print(ans)


if __name__ == '__main__':
    main()
