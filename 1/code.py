s = open('24-223.txt').readline() 
k = kmax = c = cmax = 0 
s = s.replace('AB', '*').replace('CAC', '%') 
for i in range(len(s)): 
   if s[ i] == '*': 
       k += 2 
   elif s[ i] == '%': 
       k += 3 
   else: 
       kmax = max(kmax, k) 
       k = 0 
kmax = max(kmax, k) 
print(kmax)
 
