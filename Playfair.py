key = ['m','o','n','a','r','c','h','y']
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


main = ['m','o','n','a','r','c','h','y','b','d','e','f','g','i','k','l','p','q','s','t','u','v','w','x','z']


k = 5
matrix = [main[i * k:(i + 1) * k] for i in range((len(main) + k - 1) // k )]  
print (matrix)


'''
for i in range(len(alpha)):
    if (alpha[i] in key):
        break
    else:
        key.extend(alpha[i])

print(key)'''




plain = 'haesmaiprkpv'

t = []

for i in range(len(plain)):
    t.append(main.index(plain[i]))

print(t)

n = 2
rowdivide = [t[i * n:(i + 1) * n] for i in range((len(t) + n - 1) // n )]  
print (rowdivide)




'''n = 2
rowdivide = [plain[i * n:(i + 1) * n] for i in range((len(plain) + n - 1) // n )]  
print (rowdivide)

print(rowdivide[2][1])'''

row = []
column = []


for i in range(len(rowdivide)):
    for j in range(len(rowdivide[0])):
        row.append(int(rowdivide[i][j]/k))
        column.append(rowdivide[i][j]%k)


print(row)
print(column)

for i in range(0,len(row),2):
    if(row[i] == row[i+1]):
        print(matrix[row[i]][column[i]+1])
        print(matrix[row[i]+1][column[i]+2])

        #print(row[i])
        #print(column[i]+1)

        #[(row[i]*5 + [column[i+1]])]

        #print(main[int(row[i]*5 + column[i+1])])
    
    elif(column[i] == column[i+1]):
        print(matrix[row[i]+1][column[i]])
        print(matrix[row[i]+2][column[i]])
        #print('hhhh')
        
    else:
        #print('ggggg')


        #print(row[i]*5 + column[i])
        #print(row[i+1]*5 + column[i+1])

        #main[row[i]*5 + column[(5-i)]]
        #main[row[i+1]*5 + column[(5-i-1)]]

        
        #print(matrix[row[i]][column[(5-i)]])
        #print(matrix[row[i]+1][column[(5-(i+1))]])

        print(column[(5-(i+1))])

        

        


    

