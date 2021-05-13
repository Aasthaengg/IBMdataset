w = input()

cnt_dict = {}
for c in w:
    if c not in cnt_dict.keys():
        cnt_dict[c] = 0
    cnt_dict[c] += 1

ans = "Yes"
for c in cnt_dict.keys():
    if cnt_dict[c] % 2 == 1:
        ans = "No"
        break
print(ans)
