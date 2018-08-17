def lessThan4(aList):
    ''' 
    aList: a list of strings
    '''
    subList = []
    for string in aList:
        if len(string) < 4:
            subList.append(string)
    return subList