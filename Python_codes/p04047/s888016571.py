n = int(input())
 
arr = list(map(int, input().split()))

arr.sort()

res = 0
i=0
l = len(arr)
while i<l:
  res+=min(arr[i], arr[i+1])
  i+=2
  
print(res)
