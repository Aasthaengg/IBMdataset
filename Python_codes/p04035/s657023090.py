import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import itertools

# 和がL以上の2つをつなぐ
# 和がL以上のものが1つ作れたら、その周辺だけ処理していけばよい

N,L,*A = map(int,read().split())

S = [0] + [x+y for x,y in zip(A,A[1:])]
M = max(S)
i = S.index(M)

if M < L:
    print('Impossible')
    exit()

answer = list(itertools.chain(range(i,0,-1),range(i+1,N)))[::-1]
print('Possible')
print('\n'.join(map(str,answer)))