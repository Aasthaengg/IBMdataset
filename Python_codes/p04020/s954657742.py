def solve(N, A):
    ret = 0
    for idx in range(N):
        ret += A[idx] // 2
        A[idx] %= 2
        if A[idx] and idx + 1 < N and A[idx + 1]:
            ret += 1
            A[idx + 1] -= 1
    return ret

if __name__ == "__main__":
    N = int(input())
    A = [0 for _ in range(N)]
    for idx in range(N):
        A[idx] = int(input())
    print(solve(N, A))