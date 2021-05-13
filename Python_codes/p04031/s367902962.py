import numpy as np

n=input()
a=[int(x) for x in input().split()]

a_min=np.min(a)
a_max=np.max(a)

cost_list=[]
for i in range(a_min, a_max+1):
  
  cost=0
  for val in a:
    cost+=(val-i)**2
    
  cost_list.append(cost)
  
min_cost=np.min(cost_list)

print(min_cost)