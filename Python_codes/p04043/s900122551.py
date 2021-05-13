def main():
    lst = list(map(int, input().split()))
    lst.sort()

    if lst == [5, 5, 7]:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
