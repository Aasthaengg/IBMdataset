s = input()

lst = []

for i in range(len(s)):
   lst.append(s[i])

lst2 = list(set(lst))

result = 'Yes'

for i in lst2:
   if lst.count(i) % 2 != 0:
      result = 'No'

print(result)