import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


s = input()
v1 = ("N" in s) + ("S" in s)
v2 = ("W" in s) + ("E" in s)
if v1==1 or v2==1:
    ans = "No"
else:
    ans = "Yes"
print(ans)