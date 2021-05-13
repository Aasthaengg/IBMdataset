#!/usr/bin/env python3
import re

s = input()
for i in range(5):
    s = re.sub(r"\dB", "", s)
print(s.replace("B", ""))
