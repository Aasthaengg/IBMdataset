def main():
    N, L = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(1, N):
        if A[i-1] + A[i] >= L:
            print("Possible")
            for j in range(1, i):
                print(j)
            for j in range(N-1, i-1, -1):
                print(j)
            return
    print("Impossible")


if __name__ == "__main__":
    main()
