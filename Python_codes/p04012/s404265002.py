str_line = input()
str_line = list(str_line)
str_line.sort()
#print(str_line)
temp = 0
stnum_list = []

for i in range(1,len(str_line)-1):
    if str_line[i] == str_line[i-1]:
        temp += 1
        
    else:
        stnum_list.append(temp)
        temp = 0
        

rsult = 1
#print(len(str_line))

if len(str_line) == 1:
    rsult = 0
else:
    for i in range(len(stnum_list)):
        rsult *= stnum_list[i]

if rsult%2 == 1:
    print("Yes")
else:
    print("No")