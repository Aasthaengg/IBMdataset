import sys

kushiYaki = int(input())

kushi = list(map(int, input().split()))

kushi.sort()

max_ingredients = 0

for available_ingredient in kushi[0::2]:
    max_ingredients += available_ingredient

print(max_ingredients)
