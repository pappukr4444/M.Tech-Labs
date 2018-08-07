a = [str(x) for x in input().split()]
print(a)

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
    
    
print(b)
print(c)

#for key in range(25):
    
for i in range(len(c)):
    d.append(((int(ord(c[i]) - 96) - k) % 26) + 96)
    e.append(chr(d[i]))
        #print(chr(d[i]))    

    
print(d)
print(e)    
