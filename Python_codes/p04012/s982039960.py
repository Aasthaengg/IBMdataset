w=input()
l=[0]*26
for i in range(len(w)):
  l[ord(w[i])-97]+=1
for j in range(26):
  if l[j]%2==1:
    print("No")
    break
else:
  print("Yes")