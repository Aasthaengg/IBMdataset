import sys
input = sys.stdin.readline
n = int(input())
As = [int(input()) for i in range(n)]

ans = 0
for i in range(n-1):
    ans += As[i] // 2 
    As[i] = As[i] % 2
    if As[i] == 1 and As[i+1] > 0:
        As[i+1] -= 1
        ans += 1
ans += As[n-1]//2    

print(ans)