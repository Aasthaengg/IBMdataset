number = int(input())

candy = 0

for i in range(number):
    candy_add = i + 1
    candy = candy + candy_add

print(candy)