#KNOT PUZZLE
N,L=map(int,input().split())
lists=list(map(int,input().split()))
flag=False
J=0
for i in range(N-1):
    if lists[i]+lists[i+1]>=L:
        J=i+1
        flag=True
        break
if not flag:
    print("Impossible")
if flag:
    print("Possible")
    for i in range(100001,0,-1):
      if 1<=J-i<=N-1:
        print(J-i)
      if 1<=J+i<=N-1:
        print(J+i)
    print(J)
      
    




    

