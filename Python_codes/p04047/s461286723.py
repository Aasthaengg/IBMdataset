# AGC001A - BBQ Easy
def main():
    N, *L = map(int, open(0).read().split())
    L.sort()
    ans = sum(L[::2])
    print(ans)


if __name__ == "__main__":
    main()