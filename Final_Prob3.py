def sum_digits(s):
    """ assumes s a string
    Returns an int that is the sum of all of the digits in s.
        If there are no digits in s it raises a ValueError exception."""
    digit_in_s = False
    for char in s:
        try:
            int(char)
            digit_in_s = True
        except:
            pass
    
    if len(s) == 0 or not digit_in_s:
        raise ValueError('no digits in s')
    else:
        i = 0
        sum = 0
        while i < len(s):
            try: 
                sum += int(s[i])
                i += 1
            except:
                i += 1
        return sum
                
        