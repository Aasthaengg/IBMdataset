n,a=map(int,input().split())
x=list(map(int,input().split()))
for i in range(len(x)):
    x[i]-=a
li=[[0]*5001 for i in range(n+1)]
for i in range(n):
    li[i+1][2500+x[i]]+=1
    for j in range(5001):
        if li[i][j]>=1:
            li[i+1][j+x[i]]+=li[i][j]
            li[i+1][j]+=li[i][j]
    # print(li[i+1][2490:2510])
print(li[n][2500])