def main():
    N, L = list(map(int, input().split()))
    A = list(map(int, input().split()))
    max_len_knot, max_len = - 1, 0
    for i in range(N - 1):
        if A[i] + A[i + 1] > max_len:
            max_len_knot = i
            max_len = A[i] + A[i + 1]
    if max_len < L:
        print('Impossible')
    else:
        print('Possible')
        for i in range(max_len_knot):
            print(i + 1)
        for i in range(N - 2, max_len_knot, -1):
            print(i + 1)
        print(max_len_knot + 1)


if __name__ == '__main__':
    main()