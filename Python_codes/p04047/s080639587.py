n = int(input())*2
arr = list(map(int, input().split()))
arr = sorted(arr)
sum = 0
for i in range(0,n,2):
  sum += arr[i]
print(sum)