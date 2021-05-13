n = int(input())
l = list(map(int,input().split(" ")))

cost_list = []

for i in range (-100,101):
    cost = 0
    for j in l:
        cost += (j - i)**2
    cost_list.append(cost)
cost_list.sort()
print(cost_list[0])