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
print((a*(a+1))//2)

