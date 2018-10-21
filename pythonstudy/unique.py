ls = [1,3,5,7,9,7,5,3,1]

def unique1(ls):
    newlst = []
    for i in ls:
        has = False
        for j in newlst:
            if i==j: has = True
        if not has:
            newlst.append(i)
    return newlst

def unique2(ls):
    newlst = []
    for i in ls:
        if not i in newlst:
            newlst.append(i)
    return newlst

print(unique1([1,1,2,2,1,2]))
print(unique2([1,1,2,2,1,2]))
print(list(set([1,1,2,2,1,2])))
