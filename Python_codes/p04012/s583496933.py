w=input()
count=[0]*26
ans="Yes"
for i in range(len(w)):
    count[ord(w[i])-97]+=1
for i in range(26):
    if count[i]%2==1:
        ans="No"
        break
print(ans)