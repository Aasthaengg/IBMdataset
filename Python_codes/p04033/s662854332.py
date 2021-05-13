a,b =map(int,input().split())
cnt =b-a+1

if a <0 and b>0 or a==0 or b==0:
    ans = "Zero"
elif (a>0 and b>0) or(a<0 and b<0 and cnt%2==0) :
    ans="Positive"
    
elif(a<0 and b<0 and cnt%2!=0):
    ans="Negative"
    
print(ans)