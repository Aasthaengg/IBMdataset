l = list(map(int, input().split()))

counter5 = 0
counter7 = 0

for num in l:
    if num == 5:
        counter5+=1
    
    if num == 7:
        counter7+=1

if counter5 == 2 and counter7 == 1:
    print("YES")

else:
    print("NO")