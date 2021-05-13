N=int(input())
inp=input()
L=[int(val) for val in inp.split()]
L=sorted(L,reverse=True)
total=0
start=0
for _ in range(N):
  total+=min(L[start],L[start+1])
  start+=2
print(total)
