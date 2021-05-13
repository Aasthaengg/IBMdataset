import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def S(): return sys.stdin.readline().rstrip()

N,L = LI()
S = [S() for i in range(N)]
S.sort()
print(''.join(S))