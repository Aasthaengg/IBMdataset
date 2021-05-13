q = int(input())

l = [int(x) for x in input().split(' ')]

avarage = round(sum(l)/q)

cost = 0
for i in range(q):
    cost += (l[i]-avarage)**2

print(cost)