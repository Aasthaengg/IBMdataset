import sys
def input(): return sys.stdin.readline().strip()
def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N = Z()
    A = [Z() for _ in range(N)]
    output = 0

    def makeRun(i, s):
        #A[i]とA[i+1]でシュンツ作る
        if A[i] <= 0 or A[i+1] <= 0: return s
        A[i] -= 1
        A[i+1] -= 1
        s += 1
        return s

    def makeTriple(i, s):
        #A[i]でコーツ作る
        if A[i] < 0: return s
        s += A[i]//2
        A[i] %= 2
        return s

    for i in range(N-1):
        if A[i]%2: output = makeRun(i, output)
        output = makeTriple(i, output)
    output = makeTriple(N-1, output)
    print(output)

    return

if __name__ == '__main__':
    main()
