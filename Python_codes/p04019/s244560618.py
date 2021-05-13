s = list(set(list(input())))

if (len(s)%2==1):
      print("No")
else:
      if ("N" in s) and ("S" in s):
            print("Yes")
      elif ("E" in s) and ("W" in s):
            print("Yes")
      else:
            print("No")
