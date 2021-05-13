n,l=map(int,input().split())
t=list(map(int,input().split()))
for i in range(n-1):
    if t[i]+t[i+1]>=l:
        print('Possible')
        print(*(list(range(1,i+1))+list(range(n-1,i+1,-1))),sep='\n')
        print(i+1)
        exit()
print('Impossible')