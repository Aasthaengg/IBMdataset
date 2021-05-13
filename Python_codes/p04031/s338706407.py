from statistics import mean 
import math
n=int(input())
arr=[int(x) for x in input().split()]
a=math.ceil(mean(arr))
b=math.floor(mean(arr))
s1=0
s2=0
for x in arr:
    s1=s1+((x-a)**2)
    s2=s2+((x-b)**2)
print(min(s1,s2))
