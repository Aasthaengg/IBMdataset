import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N,*L = map(int,read().split())

L.sort()
answer = sum(L[::2])
print(answer)