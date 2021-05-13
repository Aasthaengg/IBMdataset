N,L=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
possible=0
for i in range(N-1):
    if(a[i]+a[i+1] >= L):
        print("Possible")
        possible=i+1
        break
if(possible):
    for i in range(1,possible):
        print(i)
    for i in range(N-possible-1):
        print(N-i-1)
    print(possible)
else:
    print("Impossible")
