import sys
bbn=1000000007
	
#+++++

		
def main():
	n = int(input())
	l=[0]*(n+1)
	for i in range(n):
		a=int(input())
		l[i]=a

	ret=0
	for i in range(n):
		ret += l[i] // 2
		if l[i]%2==1 and l[i+1]>=1:
			ret+=1
			l[i+1]-=1
	print(ret)
	
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)

if __name__ == "__main__":
	if sys.platform =='ios':
		sys.stdin=open('inputFile.txt')
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)