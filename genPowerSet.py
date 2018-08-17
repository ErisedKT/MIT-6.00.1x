from itertools import combinations

def powerSet(items):
    ''' 
    Input:
        items: list
    
    Yields one subset of items at a time
    '''
    N = len(items)  #number of items in the list
    
    for r in range(N+1):    # taking elements in list r at a time
        for elt in list(combinations(items, r)):
            yield list(elt)    # generating subsets of items 1 at a time


        
