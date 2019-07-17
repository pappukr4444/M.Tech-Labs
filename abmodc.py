# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 14:31:28 2018
￼
@author: Puneet Kumar
"""
import math
import numpy as np
￼
#a = eval(input("a = "))

#b = eval(input("b = "))

#c = eval(input("c = "))

a,b,c = 5,117,19￼

#a=117
bin = [int(x) for x in bin(b)[2:]]
print(bin)
   
l = [a % c]

index = len(bin)￼￼

for i in range(1,index):
    #l.append(i)
    l.append((l[i-1] * l[i-1]) % c)
    
    
print(l)
    
for j in range(index):
    #print(j)
    print(j)
