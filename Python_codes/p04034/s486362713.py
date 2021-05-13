import sys
sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline    ####
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def printlist(lst, k='\n'): print(k.join(list(map(str, lst))))
INF = float('inf')

def solve():
    n, m = MI()

    B = [1] * n
    J = [False] * n
    J[0] = True

    for i in range(m):
        x, y = MI1()

        if J[x] == True:
            if B[x] == 1:
                J[x] = False
            B[x] -= 1
            J[y] = True
            B[y] += 1
        else:
            if B[x] > 0:
                B[x] -= 1
                B[y] += 1
    print(sum(J))





if __name__ == '__main__':
    solve()
