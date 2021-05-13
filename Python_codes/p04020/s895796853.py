import sys
def input():return sys.stdin.readline().strip()

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    ans = 0

    for i in range(N-1):
        if A[i] >= 2:
            ans += A[i]//2
        if A[i]%2 == 1 and A[i+1] >= 1:
            ans += 1
            A[i+1] -= 1
    
    ans += A[N-1]//2
    print(ans)
if __name__ == "__main__":
    main()