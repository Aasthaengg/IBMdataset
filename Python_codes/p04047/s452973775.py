num_meals = int(input())
skewers = list(map(int, input().split()))
skewers.sort()
ingredients = 0
for skewer in range(0,(len(skewers) - 1),+2):
    ingredients = ingredients + skewers[skewer]
print(ingredients)
