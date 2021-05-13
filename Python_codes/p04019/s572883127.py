#!/usr/bin/env python3
s = input()
s = {i for i in s}
if len(s) == 4 or s == {"N", "S"} or s == {"W", "E"}:
    print("Yes")
else:
    print("No")
