N,L=map(int,input().split())
List = []
for i in range (N):
  List.append(str(input()))
List.sort()
res = ""
for i in range(N):
  res+=List[i]
print(res)