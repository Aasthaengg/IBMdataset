def main():
  a,b,c=map(int,input().split())
  li=[a,b,c]
  if sorted(li)==[5,5,7]:
    print('YES')
  else:
    print('NO')
  
if __name__=="__main__":
  main()