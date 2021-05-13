w=input()
d={}
for i in range(int(len(w))):
    if w[i] not in d:
        d[w[i]]=1
    else:
        d[w[i]]+=1
for i in d.values():
    if i%2==1:
        print("No")
        exit()
print("Yes")