def cin():
	return map(int,input().split())

def cino(test=False):
    if not test:
        return int(input())
    else:
        return input()
def cina():
  return list(map(int,input().split()))

a = cino()
l = cina()
ans = 10**18
for i in range(-100,101):
    cost = 0
    for j in range(len(l)):
        cost += (i-l[j])**2
    ans = min(ans,cost)
print(ans)


