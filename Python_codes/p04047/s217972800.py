import sys
import os
if sys.platform=="darwin":
	base = os.path.dirname(os.path.abspath(__file__))
	name = os.path.normpath(os.path.join(base, '../Documents/input.txt'))
	#print(name)
	sys.stdin = open(name)

n = int(input())
l = list(map(int,input().split()))

l = sorted(l)
#print(l)
#print( l[::2] )
print( sum(l[::2]) )
