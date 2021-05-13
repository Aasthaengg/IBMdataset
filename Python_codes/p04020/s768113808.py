def main():
  n = int(input())
  bef = 0
  ans = 0
  for i in range(n):
    now = int(input())
    ans += min(bef, now)
    now -= min(bef, now)
    ans += now//2
    bef = now % 2
  print(ans)
  
if __name__ == "__main__":
  main()