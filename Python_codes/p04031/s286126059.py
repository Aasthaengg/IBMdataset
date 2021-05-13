N=int(input())
alist=list(map(int,input().split()))

min_answer=float("inf")
for i in range(min(alist),max(alist)+1):
  answer=0
  for a in alist:
    answer+=(a-i)**2
    
  min_answer=min(answer,min_answer)
print(min_answer)