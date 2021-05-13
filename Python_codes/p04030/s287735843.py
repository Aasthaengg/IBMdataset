S = list(input())
ans = ""

for s in S:
    if s == "B":
        ans = ans[:len(ans) - 1]
    else:
        ans += s
        
print(ans)