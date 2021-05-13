import numpy as np   
n,m = [int(i)for i in input().split()]

l = [[int(i)-1 for i in input().split()] for _ in range(m)]

line = np.array([1 for _ in range(n)])
is_red = np.zeros(n,dtype = np.int32)
is_red[0] = 1

for x,y in l:
    line[x] -= 1 if line[x] > 0 else 0
    line[y] += 1
    is_red[y] = 1 if is_red[x] == 1 else is_red[y]
    is_red[x] = is_red[x] if line[x] > 0 else 0
    

ans = np.count_nonzero(is_red[line > 0])

print(ans)
    

    
