#ABC043C
n=int(input())
a = list(map(int, input().split()))
h=round(sum(a)/len(a))
sum_a=0
for i in range(len(a)):
    sum_a=sum_a+(a[i]-h)**2
print(int(sum_a))