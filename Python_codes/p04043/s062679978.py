A,B,C=map(int,input().split())
sum = 0
if A == 5 or A ==7:
  sum += A
  if B ==5 or 7:
    sum += B
    if C ==5 or 7:
      sum += C
      if sum == 17:
        print("YES")
      else:
        print("NO")