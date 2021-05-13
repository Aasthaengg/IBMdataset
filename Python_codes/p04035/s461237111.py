n,l = map(int,input().split())
a = list(map(int,input().split()))
for i in range(n-1):
    if a[i]+a[i+1]>=l:
        print('Possible')
        ans = list(range(1,i+1))+list(range(i+2,n))[::-1]
        ans.append(i+1)
        for i in ans:
            print(i)
        exit()
print('Impossible')
