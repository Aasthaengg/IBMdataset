s = sorted(list(set(input())))

if len(s) == 1 or len(s)==3: ans = "No"
elif len(s) == 2 or len(s)==4:
    if s == ["N","S"] or s == ["E", "W"]: ans = "Yes"
    elif s == ["E", "N", "S", "W"]: ans = "Yes"
    else: ans = "No"
print(ans)