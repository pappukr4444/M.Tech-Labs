
#se = int(seed[0][tag_postion])

#print(len(seed))
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:37:53 2018

@author: Puneet Kumar
"""
'''
a = ['a','b','c','d','e']

k = ['a','y','u','s','h']

b =[]
c= []

for i in range(len(a)):
    b.append((int((ord(a[i]) - 96) + (ord(k[i]) - 96)) % 26) + 96)
    #c.append(chr(b[i]))
print(b)
'''

#print(b)
#print(c)
    
    
#a = ['a','b','c','d','e']
#a = input("Enter the Massage : ")
'''
with open('ram.txt','r') as f:
    a = f.read()
'''
a = 'hello'

k = "ayush"

#k = input("enter the key of text: ")
#k = ['a','y','u','s','h']

b =[]
c= []

for i in range(len(a)):
    b.append((int((ord(a[i]) - 96) + (ord(k[i]) - 96)) % 26) + 96)
    c.append(chr(b[i]))
#print(b)
print(c)

d = []
e = []

for i in range(len(c)):
    d.append((int((ord(c[i]) - 96) - (ord(k[i]) - 96)) % 26) + 96)
    e.append(chr(d[i]))
#print(b)
print(e)