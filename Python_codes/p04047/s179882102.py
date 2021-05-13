# AGC 001: A – BBQ Easy
n = int(input())
l = [int(s) for s in input().split()]

l.sort()
total_number = 0

for i in range(0, n * 2, 2):
    total_number += l[i]

print(total_number)