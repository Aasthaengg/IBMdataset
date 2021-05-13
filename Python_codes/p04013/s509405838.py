n,a = map(int, raw_input().split())
ais = map(int, raw_input().split())
mem = {}
def dfs(i,ais, cumul,count,a):
	if i == len(ais):
		return 1 if (count > 0 and count * a == cumul) else 0
	if (i,cumul,count) in mem:
		return mem[(i,cumul,count)]
	mem[(i,cumul,count)] = dfs(i+1, ais, cumul + ais[i], count +1, a) + dfs(i+1, ais, cumul, count, a)
	return mem[(i,cumul,count)]
print dfs(0,ais,0,0,a)