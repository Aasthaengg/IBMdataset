def main():
  N,L=map(int,input().split())
  a=[input() for _ in range(N)]
  print(''.join(sorted(a)))

if __name__=="__main__":
  main()