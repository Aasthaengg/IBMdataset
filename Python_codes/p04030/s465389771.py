def main():
  s=input()
  a=[]
  for i in range(len(s)):
    if s[i]=='0':
      a.append('0')
    elif s[i]=='1':
      a.append('1')
    elif s[i]=='B':
      if a==[]:
          continue
      else:
          a.pop(-1)
  print(''.join(a))
  
  
if __name__=='__main__':
  main()