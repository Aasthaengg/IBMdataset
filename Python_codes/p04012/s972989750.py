def main():
    w = input()
    lst = [0] * 26

    for c in w:
        lst[ord(c) - ord("a")] += 1

    for num in lst:
        if num % 2 != 0:
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    main()
