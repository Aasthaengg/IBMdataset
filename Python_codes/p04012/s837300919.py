W=str(input())
cnt=[0 for i in range(26)]
ans="Yes"
for i in range(len(W)):
    for j in range(26):
        if ord(W[i])==97+j:
            cnt[j]+=1

for s in range(26):
    if cnt[s]%2!=0:
        ans="No"
print(ans)