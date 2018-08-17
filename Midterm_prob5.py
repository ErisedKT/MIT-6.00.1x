def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    keyList = []
    for ent in aDict:
        if aDict[ent] == target:
            keyList.append(ent)
    return sorted(keyList)