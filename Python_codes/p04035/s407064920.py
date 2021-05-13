import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n,l = map(int,readline().split())
lst1 = list(map(int,readline().split()))

res = -1

for i in range(n-1):
    if lst1[i]+lst1[i+1] >= l:
        res = i

if res == -1:
    print("Impossible")
    exit()
else:
    print("Possible")

ans = []
for i in range(res):
    ans.append(i)
for j in range(n-2,res,-1):
    ans.append(j)
ans.append(res)

for i in ans:
    print(i+1)
