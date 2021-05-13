def main():
  n=int(input())
  num = list(map(int,input().split()))
  ave=round(sum(num)/len(num))
  ans=0
  for i in range(0,len(num)):
    ans+=(ave-num[i])*(ave-num[i])
  print(ans)

main()