import collections 

w = str(input())
x = collections.Counter(w)
n = 0

    
for i in x.values():
    if i % 2 ==0:
        n += 1
        continue
    

if n == len(x.values()):
    print('Yes')

else:
    print('No')

    
