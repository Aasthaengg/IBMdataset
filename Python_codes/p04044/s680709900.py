n,l = map(int,input().split()) 
s = []
for i in range(n) :
    s.append(str(input())) 

s.sort() 
ans = ""
for i in range(n):
  ans = ans + s[i]
print(ans)