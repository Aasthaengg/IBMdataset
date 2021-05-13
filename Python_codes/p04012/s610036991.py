w = list(input())


for i in range(97, 123):
    #print("{}: {}".format(chr(i), w.count(chr(i))))
    if w.count(chr(i)) % 2 != 0:
        print("No")
        exit()

print("Yes")


    
