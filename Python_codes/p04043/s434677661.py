str_line = input().split(" ")
num_line = [int(n) for n in str_line]

num_line.sort()
#print(num_line)

if (num_line[0]==5)and(num_line[1]==5)and(num_line[2]==7):
    print("YES")
else:
    print("NO")