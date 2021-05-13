def main():
    N, L = map(int, input().split())
    S = []
    for i in range(N):
        s = input()
        S.append(s)
    S.sort()
    ans = ''.join(S)
    print(ans)

if __name__ == "__main__":
    main()
