import sys
def input(): return sys.stdin.readline().strip()

def main():
    N, L = map(int, input().split())
    S = [input() for _ in range(N)]
    S.sort()
    print("".join(S))



if __name__ == "__main__":
    main()
