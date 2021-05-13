if __name__ == "__main__":
	N, L = map(int,input().split())
	di = list()
	for i in range(N):
		di.append(input())
	copy = sorted(di)
	ans =''.join(copy)
	print(ans)