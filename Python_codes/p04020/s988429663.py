def main():
	arr =[]
	for i in range(int(input())):
		arr.append(int(input()))
	ans = 0
	now = 0
# (arr[i]+arr[i+1])//2 >= (arr[i]/2)+(arr[i+1]/2)
	for i in arr:
		if i==0:
			ans = ans +(now//2)
			now = 0
		else:
			now = now+i
	ans= ans+(now//2)
	print(ans)
if __name__ =="__main__":
	main()