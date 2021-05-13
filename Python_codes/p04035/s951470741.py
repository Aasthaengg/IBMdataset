N, L = map(int, input().split())
a = list(map(int, input().split()))

for i in range(N-1):
    if a[i]+a[i+1]>=L:
        print('Possible')
        
        ans = []
        
        for j in range(1, i+1):
            ans.append(j)
        
        for j in range(N-1, i+1, -1):
            ans.append(j)
        
        ans.append(i+1)
        
        for ans_i in ans:
            print(ans_i)
        
        break
else:
    print('Impossible')