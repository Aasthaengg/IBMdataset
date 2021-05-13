n=int(input())
a=[int(i)for i in input().split()]
b=round(sum(a)/n)
print(sum([(i-b)**2 for i in a]))