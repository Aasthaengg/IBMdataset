n, l = map(int, raw_input().split())
a = map(int, raw_input().split())
# print a
i = 0
untied  = False
while i < (len(a)-1):
    if a[i] + a[i+1] >= l:
        # print i, a[i]
        untied = True
        break
    i += 1
if untied == False:
    print "Impossible"
    exit()
print "Possible"
for k in xrange(n-1, i+1, -1):
    print k
for k in xrange(1, i+2):
    print k