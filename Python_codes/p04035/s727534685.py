N,L = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

A2 = [x+A[ind+1] for ind,x in enumerate(A[:-1])]
A2.index(max(A2))
if(max(A2)<L):
    print('Impossible')
else:
    print('Possible')
    last = A2.index(max(A2))
    for i in range(last):
        print(i+1)
    for i in range(N-1,last+1,-1):
        print(i)
    print(last+1)
