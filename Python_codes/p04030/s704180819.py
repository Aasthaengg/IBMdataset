s=input()
ans,skip='',0
for c in reversed(s):
    if c=='B':
        skip+=1
    elif skip:
        skip-=1
    else:
        ans+=c

print(ans[::-1])
