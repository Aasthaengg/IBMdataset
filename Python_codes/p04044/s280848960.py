def main():
    n, _ = map(int, input().split())
    s = [input() for _ in range(n)]
    s.sort()
    print(''.join(s))


if __name__ == '__main__':
    main()
