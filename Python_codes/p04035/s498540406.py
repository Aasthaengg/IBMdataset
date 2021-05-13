N,L=map(int,input().split())
A=list(map(int,input().split()))

for i in range(0,N-1):
    if A[i]+A[i+1]>=L:
        print('Possible')
        for j in range(1,i+1):
            print(j)
        T=[]
        for j in range(i+2,N):
            T.append(j)
        T.sort(reverse=True)
        for j in range(0,len(T)):
            print(T[j])
        print(i+1)
        break
else:
    print('Impossible')