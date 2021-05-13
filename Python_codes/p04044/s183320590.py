N,L=map(int, input().split(" "))
s=[]
for i in range(N):
    s.append(input())

s.sort()

l = ''.join([str(n) for n in s])

print(l)
