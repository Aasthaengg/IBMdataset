S=input()

n,w,s,e='N' in S,'W' in S,'S' in S,'E' in S

cand1=not n^s
cand2=not w^e

ans="Yes" if cand1 and cand2 else "No"
print(ans)
