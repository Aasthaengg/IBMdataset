import collections

s = list(input())
counter_s = collections.Counter(s)
if counter_s["N"] != 0 and counter_s["S"] == 0:
    print("No")
elif counter_s["S"] != 0 and counter_s["N"] == 0:
    print("No")
elif counter_s["W"] != 0 and counter_s["E"] == 0:
    print("No")
elif counter_s["E"] != 0 and counter_s["W"] == 0:
    print("No")
else:
    print("Yes")
