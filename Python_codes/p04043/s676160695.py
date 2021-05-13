a = list(map(int,input().split()))
answer = 'NO'
if set([5,7]) == set(a):
  if len([i for i in a if i == 5]) == 2:
    answer = 'YES'
print(answer)