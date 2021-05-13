import sys
#input = sys.stdin.readline
input = sys.stdin.buffer.readline

# mod=10**9+7
# rstrip().decode('utf-8')
# map(int,input().split())
#import numpy as np


def main():
	n,l=map(int,input().split())
	a=list(map(int,input().split()))

	for i in range(n-1):
		if a[i]+a[i+1]>=l:
			break
	else:
		print("Impossible")
		exit(0)
	i+=1
	print("Possible")
	for j in range(1,i):
		print(j)

	for j in range(n-1,i-1,-1):
		print(j)




if __name__ == "__main__":
	main()
