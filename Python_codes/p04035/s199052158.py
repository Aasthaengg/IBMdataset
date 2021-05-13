import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

"""
逆再生。長さL以上になるものをくっつけられる。
一度L以上になったらそこだけ見ていけばよい
"""

N,L = map(int,input().split())
A = [int(x) for x in input().split()]

A2 = [x+y for x,y in zip(A,A[1:])]

M = max(A2)
i = A2.index(M)
if M < L:
    answer = ['Impossible']
else:
    answer = ['Possible']
    i += 1 # ここを最後にする
    answer += [str(x) for x in range(1,i)] + [str(x) for x in range(N-1,i,-1)] + [str(i)]

print('\n'.join(answer))