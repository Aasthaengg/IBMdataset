from statistics import mean

n = int(input())

num_list = list(map(int, input().split()))

m = mean(num_list)

m = round(m)

cost = 0
for num in num_list:
    cost += (num - m)**2

print(cost)
