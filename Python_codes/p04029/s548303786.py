# -*- coding: utf-8 -*-

def main():

    N = int(input())
    ans = 0

    for i in range(N + 1):
        ans = ans + i

    print(ans)

if __name__ == "__main__":
    main()