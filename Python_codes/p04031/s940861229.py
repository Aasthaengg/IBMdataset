def main():
    n = int(input())
    A = list(map(int, input().split()))
    round = lambda x: int((x * 2 + 1) // 2)
    m = round(sum(A) / len(A))
    ans = [(a - m) ** 2 for a in A]
    print(sum(ans))

if __name__ == '__main__':
    main()