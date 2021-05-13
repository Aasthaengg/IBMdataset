import collections
w = input()
_dict = collections.Counter([x for x in w])
flag = True
for i in _dict.values():
    if i%2 == 1:
        flag = False
        break
if flag:
    print('Yes')
else:
    print('No')