# coding: utf-8
def main():
    n = int(input())
    l = sorted(map(int, input().split()))
    print(sum(l[::2]))


if __name__ == '__main__':
    main()