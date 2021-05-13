import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = [None]*n
for i in range(n):
    a[i] = int(input())
ans = 0
for i in range(n):
    num = a[i]
    if num%2==1:
        if i+1<n and a[i+1]>0:
            ans += 1
            a[i+1] -= 1
    ans += num//2
print(ans)