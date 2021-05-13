n,l=map(int,input().split())
s=[]
ss=''
for i in range(n):
	s.append(input())
s=sorted(s)
for i in range(n):
	ss+=s[i]
print(ss)