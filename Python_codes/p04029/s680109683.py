n = int(input())

count = 0

num = 1

for i in range(n):
  count += num
  num += 1

print(count)