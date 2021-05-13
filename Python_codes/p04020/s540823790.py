def main():
    n = int(input())
    A = []
    tmp = []
    ans = 0
    for _ in range(n):
        a = int(input())
        if a != 0:
            tmp.append(a)
        else:
            A.append(tmp)
            tmp = []
    if tmp != []:
        A.append(tmp)
    for a in A:
        ans += sum(a) // 2
    print(ans)

if __name__ == '__main__':
    main()
