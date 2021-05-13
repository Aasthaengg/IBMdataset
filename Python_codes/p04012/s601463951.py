w=input()
hm=lambda a,s:sum([a==x for x in s])

def isbeautiful(s):
    for a in s:
        if hm(a,s)%2==1:
            return 'No'
    return 'Yes'

print(isbeautiful(w))
