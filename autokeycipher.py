#m = 'FORTIFICATIONDEFENDTHEEASTWA'
#key = 'DEFENDTHEEASTWALLOFTHECASTLE'
#ISWXVIBJEXIGGZEQPBIMOIGAKMHE


m = 'fortificationdefendtheeastwa'

key = 'defendtheeastwallofthecastle'

#key  =  ''

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

list = ['abcdefghijklmnopqrstuvwxyz','bcdefghijklmnopqrstuvwxyza',
     'cdefghijklmnopqrstuvwxyzab','defghijklmnopqrstuvwxyzabc',
     'efghijklmnopqrstuvwxyzabcd','fghijklmnopqrstuvwxyzabcde',
     'ghijklmnopqrstuvwxyzabcdef','hijklmnopqrstuvwxyzabcdefg',
     'ijklmnopqrstuvwxyzabcdefgh','jklmnopqrstuvwxyzabcdefghi',
     'klmnopqrstuvwxyzabcdefghij','lmnopqrstuvwxyzabcdefghijk',
     'mnopqrstuvwxyzabcdefghijkl','nopqrstuvwxyzabcdefghijklm',
     'opqrstuvwxyzabcdefghijklmn','pqrstuvwxyzabcdefghijklmno',
     'qrstuvwxyzabcdefghijklmnop','rstuvwxyzabcdefghijklmnopq',
     'stuvwxyzabcdefghijklmnopqr','tuvwxyzabcdefghijklmnopqrs',
     'uvwxyzabcdefghijklmnopqrst','vwxyzabcdefghijklmnopqrstu',
     'wxyzabcdefghijklmnopqrstuv','xyzabcdefghijklmnopqrstuvw',
     'yzabcdefghijklmnopqrstuvwx','zabcdefghijklmnopqrstuvwxy',]

l = []
n = []
o = []

for i in range(len(m)):
    l.append(alpha.index(m[i]))
    n.append(alpha.index(key[i]))
    o.append(list[alpha.index(m[i])][alpha.index(key[i])])
    

print("massage to encrypt is :",m)

print("key for encrypt is :",key)

print("Encrypted massage is:",o)

#print(n)
#print(l)
'''
s = []
t = []
u = []

for i in range(len(o)):
    s.append(alpha.index(o[i]))

print(s)

for i in range(len(key)):
    #print("hello")
    print(list[s[i]])
    t.append(list[s[i]].index(key[i]))
    u.append(alpha[t[i]])


#print(list[s[1]])

print(t)

print(u)


'''