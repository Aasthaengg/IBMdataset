N,L = map(int,input().split())
A = list(map(int,input().split()))

untiable = False
lastknot = None

for i in range(N-1):
    if A[i]+A[i+1] >= L:
        untiable = True
        lastknot = i+1
        break

if untiable:
    ans = [i for i in range(1,lastknot)] + [i for i in range(lastknot+1,N)[::-1]] + [lastknot]
    print('Possible')
    print('\n'.join(map(str,ans)))
    
else:
    print('Impossible')