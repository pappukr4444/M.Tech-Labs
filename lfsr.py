#n = input("enter the n :")

sid = input("enter the seed from lfsr with space betwwen each bit:")

se = sid.split()

print(se)

print(len(se))

print(len(se)-1)

print(se[len(se)-1])

#print(n)

#print(seed)

#[int(x) for x in "1 2 3 4 5".split()]

#print(seed[0])

#tag_postion = 1

#se1 = int(se[tag_postion])

#se2 = int(se[tag_postion - 1])

#print(len(seed))

#test = (tag_postion ^ se)

#print(test)

def leftshift(seed):
    tag_postion = 1
    se1 = int(seed[tag_postion])
    se2 = int(seed[tag_postion - 1])
    for i in range(len(seed)):
        if(i==(len(seed)-1)):
            seed[(len(seed)-1)]= (se1 ^ se2)
            #print(seed[(len(seed)-1)])
        
        else:
            seed[i] = seed[i+1]
            #print(seed[i])
    return(seed)

    
#while()
seprint = leftshift(se)

#tets  = ['0','1', '1', '1', '0']
#print(seprint)

test = se ke sath comparising

print(cmp(seprint,tets))

comparising two list 

and while(!= list are not equar):
        test = seprint
        left(seprint)



    






#c = a << 2;       # 240 = 1111 0000
#print "Line 5 - Value of c is ", c
#a = 4
#c = a << 2
#d = a >> 2

#print(c)
#print(d)