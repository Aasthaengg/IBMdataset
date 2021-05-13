N, L = map(int, input().split())
a = list(map(int, input().split()))

f = 0
for i in range(N-1):
    if a[i] + a[i+1] >= L:
        f = 1
        t = i
        break
#print(t)
if f == 0:
    print("Impossible")
else:
    print("Possible")
    ans = []
    for i in range(t):
        ans.append(i+1)
    for i in range(N-1, t, -1):
        ans.append(i)
    #print(ans)
    for x in ans:
        print(str(x))
