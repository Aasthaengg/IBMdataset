from sys import stdin
def main():
    N = int(stdin.readline())
    ans = c = 0
    for _ in range(N):
        a = int(stdin.readline())
        if a:
            c += a
        else:
            ans += c >> 1
            c = 0
    print(ans + (c >> 1))
if __name__ == "__main__":
    main()