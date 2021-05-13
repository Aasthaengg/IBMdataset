def main():
    N = int(input())
    L = sorted(list(map(int,input().split())))
    LL = [L[i] for i in range(2*N) if i%2 == 0]
    print(sum(LL))

if __name__ == '__main__':
    main()