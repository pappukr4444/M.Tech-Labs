# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:30:26 2018

@author: Puneet Kumar
"""

#k = [input()]

k = ['qwertyuiopasdfghjklzxcvbnm']

#x = [input()]

#x = [str(x) for x in input("enter the text to encrypt: ").split()]

#x = 'hello'

with open('substi.txt','r') as f:
    x = f.read()
    



#print(x)

b =[]

t = []


#print(k[0][(ord(x[0]) - 96)])
#print(len(x[0]))



#for i in range(15):
#b.append(k[0][int(ord(x[1]) - 96)])

#print(k[0][int(ord(x[1]) - 96)])


#for i in range(len(x[0])):
 #   b.append(k[0][int(ord(x[0][i]) - 96)])
    #c.append(chr(b[i]))
    #print(chr(b[i]))
#print(b)

for i in range(len(x)):
    t.extend(chr(ord(x[i]) - 97))
    b.extend(k[0][int(ord(x[(i)]) - 97)])
    

str = ("".join(b))

print("The Encrypted Massage : ",str)
#print("Entrypted massage is: ",b)

with open('substi.txt','a') as f:
    f.write(str)


u = []

c = []
for j in range(len(b)):
    #print((b.index(b[j]))+97)
    #u.extend(b.index(b[j]))
    c.append(chr(((b.index(b[j])) + 97)))
    
   # u.extend(b.index(chr(ord(b[(j)]))))
    #c.extend(k[0][(int(ord(x[(i)]) + 97))% 26])
    
   # d.append(((int(ord(c[i]) - 96) - k) % 26) + 96)
    #e.append(chr(d[i]))
    
#print(u) 
str2 = ("".join(c))

print("Decrypted massage is: ",str2)

