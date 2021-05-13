N = int(input())
a = list(map(int, input().split()))
x = 100
count1 = 0
for i in a:
    count1 += (i - x)**2

for X in range(-100, 100):
    count = 0
    for i in a:
        count += (i - X)**2
    if count < count1:
        count1 = count

print(count1)
