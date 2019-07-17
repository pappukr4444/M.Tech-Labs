import math
import numpy as np

#a = eval(input("a = "))

#b = eval(input("b = "))

#c = eval(input("c = "))

a,b,c = 5,117,19

#a=117
bin = [int(x) for x in bin(b)[2:]]

#bin = [1,0,0,0,0,0,0,0,0]
print(bin)

sim = bin[::-1]

print(sim)
   
l = [a % c]

index = len(sim)

for i in range(1,index):
    #l.append(i)
    l.append((l[i-1] * l[i-1]) % c)
    
    
print(l)

temp = 1

fi = []

'''
for i in range(index,0,-1):
    if(bin[i-1] == 1):
        #temp = temp * l[i-1]
        fi.append(l[i-1])
        
print(fi)
'''

for i in range(index):
    if(sim[i] == 1):
        temp = temp * l[i]
        #fi.append(l[i])
        
print(temp)


for i in range(0,len(fi),1):
    temp = temp * fi[i]
    
    
        
print(temp)
print(temp%c)