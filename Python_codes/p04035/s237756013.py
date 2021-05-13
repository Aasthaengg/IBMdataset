import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,l = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n-1):
    if a[i]+a[i+1]>=l:
        ans = ["Possible"]
        ans += [j for j in range(1,i+1)]
        ans += [j for j in range(n-1, i+1, -1)]
        ans.append(i+1)
        break
else:
    ans = ["Impossible"]
write("\n".join(map(str, ans)))