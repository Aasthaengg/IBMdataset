# AGC001A - BBQ Easy
def main():
    n = int(input())
    L = sorted(map(int, input().rstrip().split()))
    print(sum(L[::2]))


if __name__ == "__main__":
    main()