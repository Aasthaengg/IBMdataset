
n, l = [ int(v) for v in input().split() ]
knot_list = [ int(v) for v in input().split() ]

pos = 0
for i in range(1,n):
    if knot_list[i-1] + knot_list[i] >= l:
        pos = i
        break
if pos == 0:
    print("Impossible")
else:
    print("Possible")
    for i in range(1,pos):
        print(i)
    for i in range(n-1,pos-1,-1):
        print(i)