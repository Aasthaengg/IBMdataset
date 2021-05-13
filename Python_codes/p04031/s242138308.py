n = int(input())
list_A = list(map(int, input().split()))
ans = pow(10, 10)
for num in range(-100, 101):
    list_B = list(map(lambda x:(x-num)**2, list_A))
    sum_value = sum(list_B)
    if ans > sum_value:
        ans = sum_value

print(ans)
