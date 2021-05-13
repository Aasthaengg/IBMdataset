import collections

w = list(input())
w_count = collections.Counter(w)
flag = True
for i in w_count.values():
    if i % 2 != 0:
        flag = False
if flag:
    print("Yes")
else:
    print("No")
