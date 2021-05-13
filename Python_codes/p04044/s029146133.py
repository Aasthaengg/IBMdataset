# vim: fileencoding=utf-8


def main():
    n, l = map(int, input().split())
    li = []
    for i in range(n):
        li.append(input())
    li.sort()
    print("".join(li))


if __name__ == "__main__":
    main()
