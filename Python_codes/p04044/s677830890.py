import sys
n,k = map(int, sys.stdin.readline().rstrip("\n").split())
l = [line.rstrip("\n") for line in sys.stdin]
l.sort()
s = ''.join(l)
print(s)