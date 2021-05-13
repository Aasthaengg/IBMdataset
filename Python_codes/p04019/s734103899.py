import collections


def main():
    s = list(input())
    c = collections.Counter(s)
    keys = list(c.keys())
    print("Yes" if ((keys.count("S") == 0 and keys.count("N") == 0) or (keys.count("S") == 1 and keys.count("N") == 1)) and (
        (keys.count("E") == 0 and keys.count("W") == 0) or (keys.count("E") == 1 and keys.count("W") == 1)) else "No")


if __name__ == '__main__':
    main()
