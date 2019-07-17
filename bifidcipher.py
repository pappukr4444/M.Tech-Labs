list = ['phqgmeaylnofdxkrcvszwbuti'] 

m = 'defendtheeastwallofthecastle'

row = []

column = []

for i in range(len(m)):
        t = list[0].index(m[i])
        row.append(int(t/5)+1)
        column.append((t%5)+1)
        #print(t)

#print(row)
#print(column)


n = 5

rowdivide = [row[i * n:(i + 1) * n] for i in range((len(row) + n - 1) // n )]  
print (rowdivide)


columndivide = [column[i * n:(i + 1) * n] for i in range((len(column) + n - 1) // n )]  
print (columndivide)


for i in range(len(rowdivide)):
        rowdivide[i].extend(columndivide[i])


#row.extend(column)

#print(rowdivide)

#t=2
#rowdivide1 = [rowdivide[i * t:(i + 1) * t] for i in range((len(rowdivide) + t - 1) // t )]  
#print (rowdivide1)

lst = []

iind = []


for i in range(len(rowdivide)):
        for j in range(len(rowdivide[i])):
                if(j%2 == 0):
                        lst.append(rowdivide[i][j])
                else:
                        iind.append(rowdivide[i][j])




#print(lst)

#print(iind)



#for i in range(len(lst)):

encry = []

for i in range(len(lst)):
        encry.append(list[0][(lst[i] - 1)*5 + (iind[i] - 1)])


#print(encry)

str2 = ("".join(encry))

print("The Encrypted Massage : ",str2)
