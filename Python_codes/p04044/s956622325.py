import string

alph_list=list(string.ascii_lowercase)
mydict=dict(zip(alph_list,list(range(26))))
N, L=map(int,input().split())

def compare_str(s,t):
    for i in range(L):
        if mydict[s[i]]<mydict[t[i]]:
            return '<'
        elif mydict[s[i]]>mydict[t[i]]:
            return '>'
    return '='

def newlist(w,lst):
    l=len(lst)
    pos=0
    if l==0:
        return [w]
    while l>0:
        ineq=compare_str(lst[pos+l//2],w)
        if ineq=='<' or ineq=='=':
            pos=pos+l//2+1
            l=(l-1)//2
        else:
            l=l//2
    return lst[:pos] + [w] + lst[pos:]

mylist=[]
for _ in range(N):
    mylist=newlist(input(),mylist)

print(''.join(mylist))
