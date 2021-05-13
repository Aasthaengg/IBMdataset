import sys

input=sys.stdin.buffer.readline


#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return sys.stdin.read()


def II(): return int(input())


def MI(): return map(int,input().split())


def MF(): return map(float,input().split())


def LI(): return list(map(int,input().split()))


def LF(): return list(map(float,input().split()))


def TI(): return tuple(map(int,input().split()))


# rstrip().decode('utf-8')


def main():
	n,m=MI()
	
	A=[1]*(n+1)
	B=[0]*(n+1)
	B[1]=1
	
	for _ in range(m):
		x,y=MI()
		A[x]-=1
		A[y]+=1
		
		if B[x]==1:
			B[y]=1
		if A[x]==0:
			B[x]=0

	print(sum(B))
	
	
	
	
	
	
	
	
	
	








	
	
	

if __name__=="__main__":
	main()
