from collections import Counter
W = Counter(list(input()))
flag = 0
for key in W:
    if W[key]%2!=0:
        flag = 1
        break
if flag:
    print("No")
else:
    print("Yes")