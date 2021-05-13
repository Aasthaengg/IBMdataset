n,l = map(int, input().split())
a = list(map(int, input().split()))
ans = "Impossible"
last = 0

for i in range(n-1):
    A = a[i]+a[i+1]
    if A>=l:
        ans= "Possible"
        last = i+1
        break

if ans=="Impossible":
    print(ans)
else:
    print(ans)

    if last!=1:
        for i in range(last-1):
            print(i+1)

    if last!=n-1:
        for i in reversed(range(last+1,n)):
            print(i)

    print(last)