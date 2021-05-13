S = set(list(input()))

if len(S) == 4:
    ans = "Yes"
elif len(S) == 3 or len(S) == 1:
    ans = "No"
else:
    # print(list(S))
    if ("N" in S and "S" in S) or ("E" in S and "W" in S):
        ans = "Yes"
    else:
        ans = "No"

print(ans)
