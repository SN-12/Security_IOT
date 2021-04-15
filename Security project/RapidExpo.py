#Rapid Exponentiation Recursive version
def RapidExpoRec(X, e):
    if e == 1:
        return X
    if e % 2 == 0:
        return RapidExpoRec(X, int(e/2)) * RapidExpoRec(X, int(e/2))
    else:
        return RapidExpoRec(X, int(e-1)) * X

def RapidExpo(X, e):
    e = bin(e)[3:]
    myStr = ''
    for i in e:
        if i == '0': myStr += 'S'
        else: myStr += 'SX'
    res = X
    for i in myStr:
        if i == 'S':
            res = res ** 2
        else: # i == 'X'
            res = res * X
    return res
