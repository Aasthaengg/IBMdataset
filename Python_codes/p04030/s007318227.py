import re
text = input()
b_length = len(re.sub('[^B]', '', text))
for _ in range(b_length):
    text = re.sub('(0|1)??B', '', text, 1)
print(text)