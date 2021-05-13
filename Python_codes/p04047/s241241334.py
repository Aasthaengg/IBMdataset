def main():
    N = int(input())
    L = [int(i) for i in input().split()]
    L.sort()
    print(sum(L[::2]))


if __name__ == '__main__':
    main()
