from collections import defaultdict

S = input()
dic = defaultdict(bool)
for s in S:
    dic[s] = True
if dic["N"] != dic["S"] or dic["W"] != dic["E"]:
    print("No")
else:
    print("Yes")
