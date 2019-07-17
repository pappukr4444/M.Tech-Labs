import numpy as np


alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

m = input('entre the masss:')

key = 'gybnqkurp'

l = []
n = []

for i in range(len(key)):
    l.append(alpha.index(key[i]))
print(l)


b = np.array(l)
b.resize(3, 3) # new_shape parameter doesn't have to be a tuple
print(b)

for j in range(len(m)):
    n.append(alpha.index(m[j]))
print(n)


multiply = np.matmul(b, n)

print(multiply)

t = []
l = []

for i in range(len(multiply)):
    l.append(multiply[i]%26)
    t.append(alpha[multiply[i]%26])

print(l)
print(t)

inverse_of_b = np.linalg.inv(b)

print(inverse_of_b)

multiply = np.matmul(inverse_of_b, l)

print(multiply)