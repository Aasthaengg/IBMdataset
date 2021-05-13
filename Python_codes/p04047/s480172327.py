N=input()
L=list(map(int,input().split()))

items=0

while(L):

	if L[0]<L[1] :
		s_lg=L[0]
		lg=L[1]
	else:
		s_lg=L[1]
		lg=L[0]

	if len(L)>2:
		for i in range(2,len(L)) :
			if L[i]>=lg:
				s_lg=lg
				lg=L[i]
			elif L[i]>=s_lg :
				s_lg=L[i]

	items=items+s_lg

	L.remove(s_lg)
	L.remove(lg)	

print(items)	