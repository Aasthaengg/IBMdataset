input_line = input().split()

if int(input_line[0]) + int(input_line[1]) + int(input_line[2]) != 17:
    print("NO")
    pass
elif input_line[0] == input_line[1] == "5":
    print("YES")
    pass
elif input_line[1] == input_line[2] == "5":
    print("YES")
    pass
elif input_line[0] == input_line[2] == "5":
    print("YES")
    
else:
    print("NO")

