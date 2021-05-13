from collections import defaultdict

S = input()

cnt = defaultdict(bool)
for s in S:
  cnt[s] = True

if (cnt["S"] and cnt["N"]) and (cnt["E"] and cnt["W"]):
  print("Yes")
elif (cnt["S"] and cnt["N"]) and not (cnt["E"] or cnt["W"]):
  print("Yes")
elif not (cnt["S"] or cnt["N"]) and (cnt["E"] and cnt["W"]):
  print("Yes")
else:
  print("No")
