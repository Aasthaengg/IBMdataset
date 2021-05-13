n,l = map(int, input().split())
a = list(map(int, input().split()))

sumax=0
for i in range(n-1):
    if sumax < a[i]+a[i+1]:
        sumax=a[i]+a[i+1]
        ind=i

if sumax < l:
    print("Impossible")
    exit()

print("Possible")

for i in range(1,n):
    if i>ind:
        break
    print(i)

for i in reversed(range(n)):
    if i==ind:
        break
    print(i)