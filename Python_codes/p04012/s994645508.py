S = input()
s = list(set(S))

ans = "Yes"

for i in s:
    num = S.count(str(i))
    if num % 2 == 1:
        ans = "No"

print(ans)