count = int(input())
sum_n = 0
sum_list = []

li = list(map(int, input().split(" ")))

for i in range(min(li),max(li) + 1):
  for j in li:
    sum_n += (i - j)**2
  sum_list.append(sum_n)
  sum_n = 0
    
print(min(sum_list))