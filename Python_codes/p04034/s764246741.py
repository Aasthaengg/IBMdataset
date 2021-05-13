import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	#a = int(input())
	n, m = tin()
	#s = input()
	is_red_in = [0]*n
	is_red_in[0] = 1
	num_of_ball = [1] * n
	for _ in range(m):
		f, t = tin()
		f, t = f-1, t-1
		num_of_ball[f] -= 1
		num_of_ball[t] += 1
		if is_red_in[f] == 1:
			is_red_in[t] = 1
		if num_of_ball[f] == 0:
			is_red_in[f] = 0
	return sum(is_red_in)
	
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)
		
def input_clipboard():
	import clipboard
	input_text=clipboard.get()
	input_l=input_text.splitlines()
	for l in input_l:
		yield l

if __name__ == "__main__":
	if sys.platform =='ios':
		if input_method==input_methods[0]:
			ic=input_clipboard()
			input = lambda : ic.__next__()
		elif input_method==input_methods[1]:
			sys.stdin=open('inputFile.txt')
		else:
			pass
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)