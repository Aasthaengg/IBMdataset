import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

S = input()
sS = set(S)
if "N" in sS or "S" in sS:
    if not ("N" in sS and "S" in sS):
        print('No')
        quit()
if "W" in sS or "E" in sS:
    if not ("W" in sS and "E" in sS):
        print('No')
        quit()
print('Yes')