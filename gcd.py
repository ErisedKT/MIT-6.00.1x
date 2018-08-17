def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a < b:
        result = a
    else:
        result = b
    
    while result > 0:
        if a % result == 0 and b % result == 0:
            return result
        else:
            result -= 1

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)
    
print(gcdRecur(94, 14))
            
    
