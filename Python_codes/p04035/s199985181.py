def main():
    N, L = (int(i) for i in input().split())
    A = [int(i) for i in input().split()]

    ma = 0
    idx = -1
    for i in range(N-1):
        if ma < A[i] + A[i+1]:
            ma = A[i] + A[i+1]
            idx = i+1
    if ma < L:
        return print("Impossible")
    print("Possible")
    for i in range(1, idx):
        print(i)
    for i in range(idx, N)[::-1]:
        print(i)


if __name__ == '__main__':
    main()
