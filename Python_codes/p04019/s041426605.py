S = input()
res = "Yes"
if "N" in S:
    if "S" not in S:
        res = "No"
if "W" in S:
    if "E" not in S:
        res = "No"
if "S" in S:
    if "N" not in S:
        res = "No"
if "E" in S:
    if "W" not in S:
        res = "No"
print(res)