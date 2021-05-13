children_str=input()

children=int(children_str)

candies=0

while children >= 1:
  candies=candies+children
  children=children-1
  
print(candies)