# coding: utf-8
# Your code here!
N,L=map(int,input().split())
l=list(map(int,input().split()))
judge="Impossible"
index=0

for i in range(N-1):
    if (l[i]+l[i+1])>=L:
        judge="Possible"
        index=i
        break

print(judge)
if judge=="Impossible":
    exit()

for i in range(0,index):
    print(i+1)

for i in range(index+2,N)[::-1]:
    print(i)

print(index+1)


