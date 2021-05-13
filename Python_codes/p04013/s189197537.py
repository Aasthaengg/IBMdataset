# ABC044C - 高橋君とカード / Tak and Cards (ARC060C)
def main():
    N, A, *X = map(int, open(0).read().split())
    X, D = [i - A for i in X], {0: 1}
    for i in X:
        for j, k in list(D.items()):
            D[i + j] = D.get(i + j, 0) + k
    ans = D[0] - 1
    print(ans)


if __name__ == "__main__":
    main()