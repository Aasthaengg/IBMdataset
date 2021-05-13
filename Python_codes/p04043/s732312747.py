import sys
def input(): return sys.stdin.readline().strip()

def main():
    a, b, c = map(int, input().split())
    if a == 5 and b == 5 and c == 7:
        print("YES")
        return
    if b == 5 and c == 5 and a == 7:
        print("YES")
        return
    if c == 5 and a == 5 and b == 7:
        print("YES")
        return
    print("NO")


if __name__ == "__main__":
    main()
