import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

S = read().decode()

N, W, S, E = 'N' in S, 'W' in S, 'S' in S, 'E' in S

cond1 = not N ^ S
cond2 = not W ^ E

print('Yes' if cond1 and cond2 else 'No')