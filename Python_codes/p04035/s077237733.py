N,L = list(map(int,input().split()))
a = list(map(int,input().split()))
a.append(0)
b = []
res = "Impossible"

for i in range(N):
    if L <= (a[i]+a[i+1]):
        count = i
        res = "Possible"
        break

if res =="Possible":
    for j in range(count):
        b.append(j+1)
    for k in range(count+1,N)[::-1]:
        b.append(k)
    
    print(res)
    for l in range(len(b)):
        print(b[l])
else:
    print(res)

