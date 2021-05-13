# AGC002C - Knot Puzzle
def main():
    N, L = tuple(map(int, input().split()))
    A = tuple(map(int, input().split()))
    B = [i + j for i, j in zip(A, A[1:])]
    for i, (a, b) in enumerate(zip(A, A[1:]), 1):
        if a + b >= L:
            ans = [i for i in range(1, i)]
            ans += [i for i in range(N - 1, i, -1)] + [i]
            print("Possible")
            print(*ans, sep="\n")
            break
    else:
        print("Impossible")


if __name__ == "__main__":
    main()