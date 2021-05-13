
def solve(A):
    res = 0
    b = 0
    for a in A:
        a += b
        res += a//2
        if a == b:
            b = 0
        else:
            b = a%2
    return res

if __name__ == '__main__':
    N = int(input())
    A = [int(input()) for _ in range(N)]
    print(solve(A))