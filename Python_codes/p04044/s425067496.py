n, l = map(int, input().split())
ll = []
for i in range(n):
    ll.append(input())
ll.sort()
ans = ""
for j in ll:
    ans += j

print(ans)