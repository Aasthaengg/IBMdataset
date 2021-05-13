from collections import Counter
s = input()
res = 'Yes'
for i in Counter(s).values():
    if i %  2 ==1:
        res = 'No'
print(res)