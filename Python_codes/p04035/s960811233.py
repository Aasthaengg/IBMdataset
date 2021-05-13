def main():
    n, l = map(int, input().split())
    a = list(map(int, input().split()))
    f = False
    idx = -1
    for i in range(n-1):
        if a[i] + a[i+1] >= l:
            f = True
            idx = i+1
            break
    if f:
        print("Possible")
        for i in range(1, idx):
            print(i)
        for i in reversed(range(idx+1, n)):
            print(i)
        print(idx)
    else:
        print("Impossible")

if __name__ == "__main__":
    main()