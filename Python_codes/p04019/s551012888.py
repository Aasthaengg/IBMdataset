S = input()
cannot = [
    "N" in S and "S" not in S,
    "N" not in S and "S" in S,
    "W" in S and "E" not in S,
    "W" not in S and "E" in S,
]
print("No" if any(cannot) else "Yes")