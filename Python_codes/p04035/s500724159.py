# AGC002C - Knot Puzzle
def main():
    N, L, *A = map(int, open(0).read().split())
    B = [i + j for i, j in zip(A, A[1:])]
    x = max(B)
    if x < L:  # corner case
        print("Impossible")
        return
    idx = B.index(x) + 1
    # keep the biggest one until the end
    ans = [i for i in range(1, idx)] + [i for i in range(N - 1, idx, -1)] + [idx]
    print("Possible")
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()