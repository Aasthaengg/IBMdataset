S=input()
ans='Yes'
if S.count('N')>=1 and S.count('S')==0:
    ans='No'
elif S.count('S')>=1 and S.count('N')==0:
    ans='No'
elif S.count('E')>=1 and S.count('W')==0:
    ans='No'
elif S.count('W')>=1 and S.count('E')==0:
    ans='No'
print(ans)