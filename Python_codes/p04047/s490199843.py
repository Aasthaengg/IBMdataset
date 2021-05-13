import numpy as np
N =int(input())
input_line2 =(input())
kushisashi_number = list(map(int,np.zeros(N)))

no_kushi = int(N)*2
kushi_length = list(map(int,input_line2.split()))

kushisashi=sorted(kushi_length,reverse=True)
for n in range(N):
    kushisashi_number[n] = kushisashi[2*n+1]
    
print(sum(kushisashi_number))