import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


a,b = map(int, input().split())
if a>0:
    ans = "Positive"
elif b<0:
    if (b-a+1)%2==0:
        ans = "Positive"
    else:
        ans = "Negative"
else:
    ans = "Zero"
print(ans)