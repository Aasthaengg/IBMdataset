N,L = map(int, raw_input().split())
a = map(int, raw_input().split())

for i in range(N-1):
    if a[i]+a[i+1]>=L:
        print "Possible"
        for j in range(i):
            print j+1
        for j in range(N-2,i,-1):
            print j+1
        print i+1
        break
else:
    print "Impossible"
