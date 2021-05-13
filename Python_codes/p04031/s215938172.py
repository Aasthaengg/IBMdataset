n=int(input())
a=list(map(int,input().split()))

min_cost=10000000000

for x in range(-100,101):
    i=0
    for y in a:
        i+=(y-x)**2
    min_cost=min(min_cost,i)
    
print(min_cost)