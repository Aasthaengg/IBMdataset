#C
#各ペアについてみていき、一つでもｌ以上⇔Possible

n,l = [int(i) for i in input().split()]
a   = [int(i) for i in input().split()]

maxsum=0
maxind = 0
for i in range(n-1):
    s = a[i]+a[i+1]
    if s > maxsum:
        maxsum = s
        maxind = i+1

if maxsum<l:
    print("Impossible")
else:
    print("Possible")
    for i in range(1,maxind):
        print(i)
    for i in range(n-1,maxind,-1):
        print(i)
    print(maxind)