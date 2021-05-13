S=input()
n=w=s=e=0
for c in S:
    if c=='N':
        n+=1
    elif c=='W':
        w+=1
    elif c=='S':
        s+=1
    elif c=='E':
        e+=1
ok=(n==s==0 or (n>0 and s>0)) and (w==e==0 or (w>0 and e>0))
ans="Yes" if ok else "No"
print(ans)