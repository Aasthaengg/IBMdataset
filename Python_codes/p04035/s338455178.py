import sys

N, L = map(int, sys.stdin.readline().split())
As = map(int, sys.stdin.readline().split())

tot = sum(As)

res = []

a = 0
b = N-1
for _ in range(N-1):
    if tot < L:
        print "Impossible"
        sys.exit()

    na = As[a] + As[a+1]
    nb = As[b] + As[b-1]

    if na < nb:
        #tot -= na
        tot -= As[a]
        res.append(a)
        a += 1
    else:
        #tot -= nb
        tot -= As[b]
        res.append(b-1)
        b -= 1

print "Possible"
for a in res:
    print a+1

