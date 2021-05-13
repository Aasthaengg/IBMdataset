def main():
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    print(sum(l[0::2]))


if __name__ == '__main__':
    main()

