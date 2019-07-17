# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:33:39 2018

@author: Puneet Kumar
"""
#a = [str(x) for x in input("Enter the Text: ").split()]
#print(a)3

'''with open('ram.txt','r') as f:
    a = f.read()
    #print(a)'''
a = input("enter the massage")

b = []

c = []

d = []

e = []

k = eval(input("Enter a number: "))
#k = input()

#for i in a:
    


for i in range(len(a)):
    b.append(((int(ord(a[i]) - 96) + k) % 26) + 96)
    c.append(chr(b[i]))
    #print(chr(b[i]))    
#print(b)
#print("The Encrypted Massage",c)

str = ("".join(c))

print("The Encrypted Massage : ",str)

with open('ram.txt','a') as f:
    f.write(str)

#for key in range(25):
    
for i in range(len(c)):
    d.append(((int(ord(c[i]) - 96) - k) % 26) + 96)
    e.append(chr(d[i]))
        #print(chr(d[i]))    

    
#print(d)

str2 = ("".join(e))

print("The Decrypted Massage : ",str2)
#print("The Decrypted Massage",e)   

'''f = []

t = []

g = []

for key in range(1,25):
    for j in range(len(c)):
        [f.append(chr(((int(ord(c[j]) - 96) - key) % 26) + 96))]
        #g.append(chr(f[j]))
        #print(chr(d[i]))

print(f)
#print(g)

#print(g)'''

trans = [[chr(((int(ord(c[j]) - 96) - key) % 26) + 96) for j in range(len(c))] for key in range(1,25)]

print(trans)