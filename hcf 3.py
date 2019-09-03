import factors


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

print hcf_3(2018,3027,1009)
