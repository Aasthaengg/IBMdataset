import sys
def input():
    return sys.stdin.readline()[:-1]
def main():
    a, b = map(int,input().split())
    if a > 0 and b > 0:
        print("Positive")
    elif a*b <= 0:
        print("Zero")
    else:
        if (b-a)%2 == 1:
            print("Positive")
        else:
            print("Negative")
if __name__ == '__main__':
    main()
