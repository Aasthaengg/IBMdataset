n = int(input())
a = list(map(int, input().split()))


y = 1000000


for i in range(-100, 101):
    x = 0
    for m in a:
        x += (i-m)**2
    if y > x:
        y = x

print(y)