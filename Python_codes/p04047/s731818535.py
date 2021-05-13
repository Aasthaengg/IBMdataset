def BBQ_easy(N: int, L: list)->int:
    L.sort()
    return sum(L[0::2])


if __name__ == "__main__":
    N = int(input())
    L = [int(s) for s in input().split()]

    ans = BBQ_easy(N, L)
    print(ans)
