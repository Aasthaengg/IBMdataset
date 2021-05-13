S = input()

NS = (("S" in S) & ("N" in S)) | (("S" not in S) & ("N" not in S))
EW = (("E" in S) & ("W" in S)) | (("E" not in S) & ("W" not in S))

print("Yes") if NS & EW else print("No")