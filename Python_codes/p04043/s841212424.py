a = list(map(int,input().split()))
a.sort()
if(a[0] == a[1] and a[0] == 5 and a[2] == 7): print("YES")
else: print("NO")