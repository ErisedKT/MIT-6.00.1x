import math

def polysum(n, s):
    '''
    n: number of sides
    s: length of side
    Returns area + perimeter**2 rounded to 4 decimal places
    '''
    a =  (0.25 * n * s ** 2) / math.tan(math.pi/n)
    p = n * s
    
    return round(a + p**2, 4)