n = int(input())
l = [int(i)for i in input().split()]
r = float("inf")
for i in range(-100, 101):
    r = min(r, sum((n - i)**2 for n in l))
print(r)