import random

lower = eval(input("Enter the first Range"))

upper = eval(input("Enter the second Range"))

#260 - 600

primelist = []

def prime(a,b):
    for num in range(a,b + 1):
   # prime numbers are greater than 1
       if num > 1:
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
               #print(num)
               #primelist.extend(num)
               primelist.append(num)

prime(lower,upper)

print(primelist)

length_of_list = (len(primelist) - 1)

p = primelist[(random.randint(0, length_of_list))]

q = primelist[(random.randint(0, length_of_list))]

print("value of P : ",p)
print("value of Q : ",q)

n = p * q

fi_of_n = (p-1) * (q-1)


print("value of N : ",n)

print("value of Fi of N : ",fi_of_n)


def extened(r1, r2):
        t1 = 0
        t2 = 1
        while(r1!=1 and r2!=0):
            q = int(r1/r2)
            r = r1%r2
            t = t1-q*t2
            r1 = r2
            r2 = r
            t1 = t2
            t2 = t

        while(t1<0):
            t1 = t1+fi_of_n
        return(t1)
        #print("Value of d : ",t1)
        #d = t1

e = 65537

print("value of E : ",e)

d = extened(fi_of_n,e)

print("value of D : ",d)

###==================================###
            ###Encryption###
###==================================###
m = input("enter the massage : ")
mi = []
cipher = []
#hexenc = []

for i in range(len(m)):
    mi.append(ord(m[i]))
    cipher.append((pow(mi[i],e))%n)
    #hexenc.append

print(mi)
print(cipher)




###==================================###
            ###Decryption###
###==================================###
decrypt = []
plaintext = []
hextext = []
for i in range(len(cipher)):
    #mi.append(ord(m[i]))
    decrypt.append((pow(cipher[i],d))%n)
    plaintext.append(chr(decrypt[i]))
    hextext.append(hex(decrypt[i]))
print(decrypt)
print("Decrypted massage in hex : ",hextext)
str1 = ''.join(plaintext)    
print("Decrypted Massage is : ", str1)

