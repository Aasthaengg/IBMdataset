w=input()
dic={}
for i in range(len(w)):
    x=w[i]
    if x in dic:
        dic[x]+=1
    else:
        dic[x]=1

ans="Yes"
for key in dic.values():
    if key%2==1:
        ans="No"
        break
print(ans)