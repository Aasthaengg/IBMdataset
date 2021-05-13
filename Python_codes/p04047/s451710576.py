#1
def solution(n, skewers):
  sorted_s = sorted(skewers)
  answer = 0
  for i in range(0, 2*n, 2):
    smaller = min(sorted_s[i],sorted_s[i+1])
    answer += smaller
  return answer

n = int(input())
skewers = [int(x) for x in input().split()]
print(solution(n, skewers))