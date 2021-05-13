N, L = map(int, input().split())
S = []
for i in range(N):
    S.append(input())


list.sort(S)

ans = ''.join([str(i) for i in S])
    
print(ans)