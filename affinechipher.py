#m = input('enter the mass: ')

'''with open('ram.txt','r') as f:
    m = f.read()
'''
m = input("enter the massage ")

A = eval(input("Enter a number(A): "))

B = eval(input("Enter a number(B): "))
#k = ['a','y','u','s','h']

b =[]
c= []

for i in range(len(m)):
    b.append((((int(ord(m[i]) - 96))*A + B) % 26) + 96)
    c.append(chr(b[i]))
#print(b)

#print(b)
print(c)

d = []
e = []

number = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
inverse = [1, 9, 21, 15, 3, 19, 7, 23, 11, 5, 17, 25]

t = number.index(A)

mi = inverse[t]




for i in range(len(c)):
    d.append((mi*(int((ord(c[i]) - 96) - B)) % 26) + 96)
    e.append(chr(d[i]))
#print(b)
print(e)