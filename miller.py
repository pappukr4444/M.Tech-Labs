import random

def millerTest(n,d):
        a = random.randint(2,n-2)
        #print(a)
        x = pow(a,d) % n
        if(x==1 or x == (n-1)):
            return True


n = eval(input("enter the n : "))

#print(n)
k = eval(input("enter the k : "))



if(n%2==0):
    print(n," is not prime")

# 1) Compute d and r such that d*2r = n-1
else:
    r = 0
    m = (n-1)
    while(m%2==0):
        m = m/2
        r += 1
    d=m
    print("d = ",d)
    print("r = ",r)

    for i in range(k):
        if(millerTest(n,d)==False):
            print("not prime")
        else:
            print("maybe prime")



    # 2) Call millerTest k times.
    