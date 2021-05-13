import sys
input = sys.stdin.readline

def linput(ty=int, cvt=list):
	return cvt(map(ty,input().split()))

def gcd(a: int, b: int):
	while b: a, b = b, a%b
	return a

def lcm(a: int, b: int):
	return a * b // gcd(a, b)

def dist(x1,y1,x2,y2):
	return abs(x1-x2)+abs(y1-y2)

def main():
	S = input().rstrip()
	res = 1

	n,w,s,e=[S.count(x) for x in "NWSE"]
	
	if n+s and not n*s: res=0
	if w+e and not w*e: res=0
	
	sT = "No Yes".split()
	print(sT[res])
	

if __name__ == "__main__":
	main()
