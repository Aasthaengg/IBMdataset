A = set(list(input()))
if len(A) == 2 and("S" in A and "N" in A ):
    print("Yes")
elif  len(A) == 2 and ("W" in A and "E" in A):
    print("Yes")
elif len(A) == 4:
    print("Yes")
else:
    print("No")