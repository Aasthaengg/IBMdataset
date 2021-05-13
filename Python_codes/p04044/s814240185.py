val = input()
splited_val = val.split()

val_list=[]

for x in range(int(splited_val[0])):
    val = input()
    val_list.append(val)

print("".join(sorted(val_list)))