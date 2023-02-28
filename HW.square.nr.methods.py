# HW: methods of obtaining square numbers

def square(value):
    result = value * value
    return result

def square(value):
    result = value ** 2
    return result


# pow() - function raises some value to a certain power:
# first argument is the number to raise; the second argument is the exponent
def square(value):
    result = pow(value, 2)
    return result

#########################
n = 10
n = square(n)
print(n)