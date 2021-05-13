
def main():
    N, L = map(int,input().split())
    S = [input() for _ in range(N)]
    S.sort()
    for i in S:
        print(i, end = "")


if __name__ == '__main__':
    main()
