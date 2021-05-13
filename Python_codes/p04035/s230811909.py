def main():
    import sys
    input = sys.stdin.buffer.readline
    N, L = (int(i) for i in input().split())
    A = [int(i) for i in input().split()]
    last = -1
    for i in range(N-1):
        if L <= A[i] + A[i+1]:
            last = i+1
    if last < 0:
        return print("Impossible")
    ans = [i for i in range(1, last)] + \
        [i for i in range(last+1, N)][::-1] + [last]
    print("Possible")
    print(*ans, sep="\n")


if __name__ == '__main__':
    main()
