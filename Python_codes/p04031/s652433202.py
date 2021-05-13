import sys
import math

def main():

    input()
    a = list(map(int, input().split()))

    y = round(sum(a)/len(a))

    ans = 0
    for i in a:
        ans += pow((i - y), 2)

    print(ans)


if __name__ == '__main__':
    main()