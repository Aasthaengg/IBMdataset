N = int(input())

sum_num = 0
candy = 1
for i in range(N):
    sum_num += candy
    candy += 1

print(sum_num)
