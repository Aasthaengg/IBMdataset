# AGC002C - Knot Puzzle
def main():
    N, L = tuple(map(int, input().split()))
    A = tuple(map(int, input().split()))
    B = [i + j for i, j in zip(A, A[1:])]
    x = max(B)
    if x >= L:
        idx = B.index(x) + 1
        ans = [i for i in range(1, idx)] 
        ans += [i for i in range(N - 1, idx, -1)] + [idx]
        print("Possible")
        print(*ans, sep="\n")
    else:
        print("Impossible")


if __name__ == "__main__":
    main()