import collections

s=input()
a=collections.Counter(s)
f=True

if a['N']>0:
	if a['S']==0:
		f=False
		
if a['S']>0:
	if a['N']==0:
		f=False
		
if a['W']>0:
	if a['E']==0:
		f=False
		
if a['E']>0:
	if a['W']==0:
		f=False
		
if f:
	print('Yes')
else:
	print('No')