x=input()
y = sorted(list(map(int, input().split())))
i=1
z=0
for i in range(int(len(y)/2)):
     z+=y[-2*i]
     i+=1

print(z)
