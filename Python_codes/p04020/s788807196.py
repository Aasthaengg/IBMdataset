n = int(input())

total = 0

remain = 0
c = 0
for i in range(n):
    m = int(input())
    if i > c + 1:
        remain = 0
    all_ = remain + m
    total += all_//2
    if all_ % 2 != 0 and all_//2 > 0:
        remain = all_ % 2
        c = i
print(total)