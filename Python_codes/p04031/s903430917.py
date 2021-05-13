n = int(input())
a = list(map(int,input().split()))

stock =[]

for x in range(-100,101):
    total = 0
    for i in range(n):
        total = total + (x-a[i])**2
    stock.append(total)


print(min(stock))