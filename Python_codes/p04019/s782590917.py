import collections
S=list(str(input()))
cc=collections.Counter(S)

if cc['S']==0 and cc['N']!=0:
    print('No')
elif cc['S']!=0 and cc['N']==0:
    print('No')
elif  cc['E']==0 and cc['W']!=0:
        print('No')
elif  cc['E']!=0 and cc['W']==0:
        print('No')
else:
    print('Yes')
