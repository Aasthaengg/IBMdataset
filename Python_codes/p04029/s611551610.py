N = int(input())

def dfs(n):#n人の必要な個数
    if n==1:
        return 1
    
    ans = n + dfs(n-1)
    return ans
print(dfs(N))