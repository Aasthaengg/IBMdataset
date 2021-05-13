def main():
    N, L = map(int, input().split())
    Sn = [input() for i in range(N)]
    Sn2 = sorted(Sn)
    ans = ""
    for val in Sn2 :
        ans = ans + val
    print(ans)

if __name__ == '__main__':
    main()
