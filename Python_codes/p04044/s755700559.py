# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# import math
# from itertools import *
# import random
# import calendar
import datetime
# import webbrowser

# f = open("input.txt", 'r')
# g = open("output.txt", 'w')
# n, m = map(int, f.readline().split())

n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(input())
arr.sort()
print("".join(arr))
