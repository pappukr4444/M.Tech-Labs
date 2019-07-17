'''
RC4 
Created By Punnet Kumar

'''
def swap(x, y):
    temp = x
    x = y
    y = temp

plain_text = input("enter the plain text : ")

p = []

for i in range(len(plain_text)):
    p.append((ord(plain_text[i])- 96))

print(p)



#p = [1,2,2,2]

k = [1,2,3,6]

s = [i for i in range(256)]

#print(s)

t = [k[i%len(k)] for i in range(len(s))]

#print(t)

ss = []


j = 0
for i in range(256):
    j = (j + s[i] + t[i])% 256


    temp = s[i]
    s[i] = s[j]
    s[j] = temp
    #print(j)
    

#print(s)


i = 0
j = 0
for i in range(len(p)):
    i = (i + 1)% 256
    j = (j + s[i])% 256
    swap(s[i], s[j])
    t = (s[i] + s[j])% 256
    k = s[t]
    #print(k)
    ss.append(k)

print(ss)

cipher = []
ccc = []

for i in range(len(p)):
    cipher.append((ss[i] ^ p[i]))
    ccc.append(chr(cipher[i]))



#print(ccc)
#ct=''
#ctext=ct.join(ccc)
#print('\n\n')
print('encrypted text is:',ccc)

decry = []
for i in range(len(p)):
    decry.append(chr(p[i]+96))

ct=''
ctext=ct.join(decry)
print('decrypted text is:',ctext)
#print(decry)
    
    




'''
for char in m:
    byte = ord(char)
    cipher1 = byte ^ Byte
    check.append(chr(cipher1))
    t2=''
    n=t2.join(check)
    print('reversed checked  text is:',n)

'''



'''
 j = 0
    for i in range(256):
        if len(key) > 0:
            ko=key[i % len(key)]
            km= int(ko) 
            j = (j + k[i] + km) % 256
            k[i], k[j] = k[j], k[i]
        else:
            j = (j + k[i]) % 256
'''#c = eval(input("c = "))
