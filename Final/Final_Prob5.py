def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if n
    '''
    aList = []
    vals = []
    keys = aDict.keys()
    for key in keys:
        vals.append(aDict[key])
    for key in keys:
        if vals.count(aDict[key]) == 1:
            aList.append(key)
    return sorted(aList)
        
aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}