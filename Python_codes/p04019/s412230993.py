st = input() 
n = st.count('N') 
s = st.count('S') 
e = st.count('E') 
w = st.count('W') 

if (n>0 and s==0) or (n==0 and s>0) or (w==0 and e>0) or (e==0 and w>0): 
  print("No") 
else:
  print("Yes") 