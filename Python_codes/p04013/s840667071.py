def solve(n, a, lst):
  m = max(max(lst), a)
  ans = [[[0]*(n*m+1) for i in range(n+1)] for j in range(n+1)]
  #ans[i][j][k] : lst[:i]までの中からj枚選んで合計kにする選び方
  for i in range(n+1):
    for j in range(n+1):
      for k in range(n*m+1):
        if i == 0 and j == 0 and k == 0:
          ans[i][j][k] = 1
        elif i >= 1 and k < lst[i-1]:
          ans[i][j][k] = ans[i-1][j][k]
        elif i >= 1 and lst[i-1] <= k and j >= 1:
          ans[i][j][k] = ans[i-1][j-1][k-lst[i-1]] + ans[i-1][j][k]
        else:
          ans[i][j][k] = 0
  ret = 0
  for i in range(1,n+1):
    ret += ans[-1][i][i*a]
  return int(ret)

if __name__ == "__main__":
  n, a = map(int,input().split())
  x_list = [int(i) for i in input().split()]
  ans = solve(n,a,x_list)
  print(ans)
