def resolve():
    n, l = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n - 1):
        if a[i] + a[i + 1] >= l:
            print("Possible")
            for j in range(i):
                print(j + 1)
            for j in range(n - 1, i, -1):
                print(j)
            return 0
    print("Impossible")


if __name__ == "__main__":
    resolve()
