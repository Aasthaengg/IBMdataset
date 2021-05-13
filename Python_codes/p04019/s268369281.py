s = input()
ans = "Yes"

if "N" in s:
    if "S" not in s: ans = "No" 
if "S" in s:
    if "N" not in s: ans = "No"
if "W" in s:
    if "E" not in s: ans = "No"
if "E" in s:
    if "W" not in s: ans = "No"

print(ans)