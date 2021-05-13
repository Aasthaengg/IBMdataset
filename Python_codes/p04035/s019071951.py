n, l = map(int, raw_input().split())
A = map(int, raw_input().split())

for i in xrange(n-1):
    if A[i]+A[i+1] >= l:
        print "Possible"
        print "\n".join(map(str, range(1, i+1) + range(n-1, i+1, -1) + [i+1]))
        break
else:
    print "Impossible"
