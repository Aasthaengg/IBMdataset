def main():
    N = int(input())
    L = list(map(int, input().split()))

    L = sorted(L)
    print(sum(L[::2]))

if __name__ == '__main__':
    main()