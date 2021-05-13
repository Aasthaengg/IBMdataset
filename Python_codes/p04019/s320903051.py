from collections import Counter

S = Counter(input())

if "N" in S and "S" in S and "E" not in S and "W" not in S or \
    "N" not in S and "S" not in S and "E" in S and "W" in S or \
    "N" in S and "S" in S and "E" in S and "W" in S:
    print("Yes")
else:
    print("No")
    
