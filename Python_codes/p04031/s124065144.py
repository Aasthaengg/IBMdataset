N = int(input())
ls = list(map(int,input().split()))
ave = int((sum(ls)/N*2+1)//2)
cost = 0
for i in ls:
    cost += (i-ave)**2
print(cost)