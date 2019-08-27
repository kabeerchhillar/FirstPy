def factors(num):
    hsh = []
    for x in range(1,num+1,1):
        if num % x ==  0 :
            hsh.append(x)
    return hsh

def PF(num):
    mnm = []
    for x in range(2,num+1):
        if num%x == 0:
            mnm.append(x)
            num = num/x
            while num%x == 0:
                num = num/x
                mnm.append(x)
    return mnm

def compareList( list1, list2) :
    for x in list1:
        for y in list2:
            if x == y:
                print "exists in both"
                print x
                break

def ifcoprimes():
    num1 = PF(int(raw_input("enter number 1")))
    num2 = PF(int(raw_input("enter number 2")))
    for x in num1:
        if num2.__contains__(x):
            print "they are not co prime"
            print x
    print "they are co prime"
    print num1,num2

def HCF(num1,num2):
    hcf = 1
    list1 = PF(num1)
    list2 = PF(num2)
    for x in list1:
        if list2.__contains__(x):
            hcf = hcf*x
            list2.remove(x)
    return hcf


def lcm(num1,num2):
    hcf = HCF(num1,num2)
    x = num1*num2/hcf
    return x


def main():
    num1 = int(raw_input("enter number 1"))
    num2 = int(raw_input("enter number 2"))
    print lcm(num1,num2)
    print HCF(num1,num2)

if __name__ == '__main__':
    main()

