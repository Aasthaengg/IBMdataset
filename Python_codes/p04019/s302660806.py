s= input().strip()
f="Yes"
if (s.count('N')!=s.count('S') and s.count('N')*s.count('S')==0):
    f="No"
elif(s.count('E')*s.count('W')==0 and s.count('E')!=s.count('W')):
    f="No"
print(f)