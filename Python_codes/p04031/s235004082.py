n = int(input())                                                
a_list = list(map(int, input().split()))
a_list.sort()
cost = 0
min_cost=0
 
for i in range(a_list[0], a_list[-1]):
    for j in range(len(a_list)):
        cost = cost + (a_list[j] - i)**2
 
    if i == a_list[0]:
        min_cost=cost
 
    min_cost = min(cost, min_cost)
    cost = 0
 
print(min_cost)