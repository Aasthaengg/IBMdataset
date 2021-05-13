import collections
s = input()

cnt = collections.Counter(s)

cond = True

if (cnt["N"] > 0) ^ (cnt["S"] > 0):
    cond = False
if (cnt["W"] > 0) ^ (cnt["E"] > 0):
    cond = False

print("Yes" if cond else "No")
