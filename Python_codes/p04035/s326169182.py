def slove():
    import sys
    input = sys.stdin.readline
    n, l = list(map(int, input().rstrip('\n').split()))
    a = list(map(int, input().rstrip('\n').split()))
    for i in range(1, n):
        if a[i] + a[i-1] >= l:
            print("Possible")
            for j in range(n-1, i, -1):
                print(j)
            for j in range(1, i):
                print(j)
            print(i)
            exit()
    print("Impossible")


if __name__ == '__main__':
    slove()
