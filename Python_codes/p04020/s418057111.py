n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

b = []
chain = 0
for i in range(n):
    if(chain>=1 and a[i]==0):
        b.append(chain)
        chain = 0
    elif(a[i]>=1):
        chain += a[i]
ans=0
b.append(chain)
for i in b:
    ans += i//2
    #print(i)
print(ans)



