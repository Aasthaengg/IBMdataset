def main():
    N, L, *A = map(int, open(0).read().split())
    L = [i for i,(x,y) in enumerate(zip(A, A[1:]), 1) if x+y >= L]
    if L:
        print("Possible")
        B = [i for i in range(L[0], N)]+[i for i in range(1,L[0])][::-1]
        print(*B[::-1], sep="\n")
    else:
        print("Impossible")


if __name__ == "__main__":
    main()