N = int(input())
number = list(map(int, input().split()))
total_a = 0
total_b = 0
average = sum(number)//len(number)

for i in number:
    total_a += (average-i)**2
    total_b += (average+1-i)**2

print(min(total_a, total_b))