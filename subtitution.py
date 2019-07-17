# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:30:26 2018

@author: Puneet Kumar
"""

x = input("enter the text : ")

#x = 'defgh'

k = x = input("enter the text : ")

#x = 'defgh'

k = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
'''
with open('substi.txt','r') as f:
    x = f.read()
  '''  

b =[]

t = []

for i in range(len(x)):
    t.append(k[alpha.index(x[i])])
    #b.extend(k[int(ord(x[(i)]) - 97)])

print(t)


for i in range(len(t)):
    b.append(alpha[k.index(t[i])])
    #b.extend(k[int(ord(x[(i)]) - 97)])

print(b)
    
'''
str = ("".join(b))

print("The Encrypted Massage : ",str)
#print("Entrypted massage is: ",b)

with open('substi.txt','a') as f:
    f.write(str)'''