W = input()
W_list = set(list(s for s in W))
ans = True 
for s in W_list:
    if W.count(s) % 2 != 0:
        ans = False
        break


if ans:
    print("Yes")
else:
    print("No")