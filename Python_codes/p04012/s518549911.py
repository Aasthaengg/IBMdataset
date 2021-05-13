#ABC044B
n=input()
a=[]
for i in range(len(n)):
     a.append(n[i])
sum_=0
for i2 in range(len(a)):
    sum_=sum_+a.count(a[i2])%2

if sum_ == 0:
    print("Yes")
else:
    print("No")