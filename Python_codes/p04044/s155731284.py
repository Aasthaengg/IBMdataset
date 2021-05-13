n,l=map(int,input().split())
temp =[]
for i in range(n):
  temp.append(input())
list.sort(temp)

str =""
for s in temp:
  str = str+ s

print(str)