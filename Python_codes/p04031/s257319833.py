import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))

N = I()
a = LI()

x = sum(a)//N
y = x + 1

print(min(sum((i-x)**2 for i in a),sum((i-y)**2 for i in a)))
