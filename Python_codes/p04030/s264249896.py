input = input()
output = ""

for i in range(len(input)):
    if input[i] == "0":
        output += "0"
    elif input[i] == "1":
        output += "1"
    elif input[i] == "B":
        output = output[0:len(output)-1]
    else:
        pass

print(output)