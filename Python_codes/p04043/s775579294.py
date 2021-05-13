abc = list(map(int,input().split()))
ans = "NO"
if 5 in abc:
  abc.remove(5)
  if 5 in abc and 7 in abc:
    ans = "YES"

print(ans)