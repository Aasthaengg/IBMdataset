s=input()
print('No' if 'N' in s and 'S' not in s or 'S' in s and 'N' not in s or 'W' in s and 'E' not in s or 'E' in s and 'W' not in s else 'Yes')