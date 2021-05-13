str_line = input()
str_line2 = list(str_line)
#print(str_line2)
length = len(str_line2)
line = []

for i in range(length):
    if (str_line2[i] == "1")or(str_line2[i] == "0"):
        line.append(str_line2[i])
        #print(line)
        
    else:
        if len(line) != 0:
            del line[-1]
            #print(line)
for i in range(len(line)):
    print(line[i],end="")