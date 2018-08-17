def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """  
    result = 0
    newResult = 0
    
    for ent in t:
        if type(ent) == int:
            if ent > result:
                result = ent
        else:
            newResult = max_val(ent)
            if newResult > result:
                result = newResult
    return result

            
                
                