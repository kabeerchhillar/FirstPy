import factors

def fn1test():
    rrf = []
    for x in range(2000,3200):
        if x % 7 == 0 and x % 5 != 0:
            rrf.append(x)
    return rrf

def factorial(num):
    factorial = 1
    for x in range(1,num+1):
        factorial = factorial * x
    return factorial

def printSquares(num):
    fnh = []
    for x in range(1,num+1):
        fnh.append(x*x)
    return fnh

def hcf_3(num1,num2,num3):
    hcf = 1
    list1 = factors.PF(num1)
    list2 = factors.PF(num2)
    list3 = factors.PF(num3)
    for x in list1:
        if list2.__contains__(x) and list3.__contains__(x):
            hcf = hcf * x
            list2.remove(x) and list3.remove(x)
    return hcf

#print hcf_3(2018,3027,1009)
#print fn1test()
#print factorial(8)
print printSquares(66546)