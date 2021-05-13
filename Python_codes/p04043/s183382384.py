from functools import reduce
A= list(map(int,input().split()))
sum= reduce(lambda a,b : a+b, A)
if(sum==17):
    print("YES")
else:
    print("NO")
