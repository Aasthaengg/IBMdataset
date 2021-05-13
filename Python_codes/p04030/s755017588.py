S = list(input())
Ans = []
for s in S:
    if s == "0":
        Ans.append("0")
    elif s == "1":
        Ans.append("1")
    else:
        if Ans:
            Ans.pop()
print("".join(Ans))