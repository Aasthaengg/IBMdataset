S = input()
es =''
for s in S:
    if s == '1' or s == '0':
        es+=s
    else:
        if es != '':
            es=es[:-1]
print(es)