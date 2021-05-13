import bisect,collections,copy,heapq,itertools,math,numpy,string
from fractions import gcd
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split())) # tupleも検討する。
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    N = S()
    L = [i for i in N]
    ans = []

    for i, num in enumerate(L):
        if(num != "B"):
            ans.append(num)
        if(ans != [] and num == "B"):
            ans.pop(-1)

    print("".join(ans))

if __name__ == '__main__':
    main()