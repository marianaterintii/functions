#create functions that corespond to: * / + -

def mul (a, b):
    return a * b

def div (a, b):
    return a / b

def add (a, b):
    return a + b

def sub (a, b):
    return a - b



r = mul (10, 100)
print (r)

r = div (10, 100)
print (r)

#HW1: finish add and sub
r = add (10, 100)
print (r)

r = sub (10, 100)
print (r)

#HW: rewrite

def calc (a, b, c, d ):
    return a + b * c / d

r = calc (1, 2, 3, 4)
print (r)
