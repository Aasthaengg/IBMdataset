N,L = map(int,input().split())
A = list(map(int,input().split()))

flg = 0
for i in range(N-1):
    if A[i] + A[i+1] >= L:
        last = i
        flg = 1
        break

if flg == 0:
    print('Impossible')
else:
    print('Possible')
    last += 1
    # x = list(range(last+1,N))
    x = list(range(N-1,last,-1))
    y = list(range(1,last))
    for a in x:
        print(a)
    for a in y:
        print(a)

    print(last)
