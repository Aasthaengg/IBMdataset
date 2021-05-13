s = list(input())
ans = [""] * 10
ptr = 0
for c in s:
    if c == "B":
        ptr = max(0,ptr-1)
    else:
        ans[ptr] = c
        ptr += 1

print("".join(ans[:ptr]))
        
