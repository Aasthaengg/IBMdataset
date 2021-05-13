n=int(input())
l=list(map(int,input().split()))
cost=[]
for i in range(-100,101):
    count=0
    for j in l:
        count+=(j-i)**2
    cost.append(count)
print(min(cost))