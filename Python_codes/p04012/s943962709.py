w = input()
beau = {}
for i in range(len(w)):
    if not w[i] in beau:
        beau[w[i]] = 1
    else:
        beau[w[i]] += 1
num = sum(list(map(lambda x: x%2,list(beau.values()))))
if num == 0:
    print('Yes')
else:
    print('No')