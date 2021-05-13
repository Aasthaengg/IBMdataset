
def know(N, K, A):
    isOK = False
    for i in range(1, N):
        if A[i] + A[i - 1] >= K:
            isOK = True
            first = i

    if not isOK:
        return ["Impossible"]

    ans = [first]
    for i in range(first + 1, N):
        ans.append(i)
    for i in range(first - 1, 0, -1):
        ans.append(i)
    return ["Possible"] + ans[::-1]


if __name__ == "__main__":
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = know(N, K, A)
    print(*ans, sep="\n")
