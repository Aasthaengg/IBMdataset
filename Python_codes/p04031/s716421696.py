
n = int(raw_input())
ais = map(int, raw_input().split())
ais.sort()

def f(ais):
	return [sum(ais)/len(ais),sum(ais)/len(ais)+1,sum(ais)/len(ais)-1]
	if len(ais) % 2:
		return [ais[len(ais)/2]]
	
	v = ais[len(ais)/2 -1] + ais[len(ais)/2]
	return [v/2,v/2-1,v/2+1]
def g(ais,m):
	s= 0
	for ai in ais: s+=abs(ai - m) **2
	return s
print min([g(ais,m) for m in f(ais)])