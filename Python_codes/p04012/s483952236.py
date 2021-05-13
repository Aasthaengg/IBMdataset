w = str(input())
dic = {}
for s in w:
    dic.setdefault(s,0)
    dic[s] += 1
#print(dic)
isOK = True
for i in dic.values():
    if i % 2 != 0:
        isOK = False
        break
if isOK:
    print('Yes')
else:
    print('No')
