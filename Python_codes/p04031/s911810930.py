
n = int(raw_input())
ais = map(int, raw_input().split())
ais.sort()
vv= sum(ais)/len(ais)
def g(ais,m):
	s= 0
	for ai in ais: s+=abs(ai - m) **2
	return s
print min([g(ais,m) for m in [vv+dela for dela in [-1,0,+1]]])