animals = {'b': [1, 7, 5, 4, 3, 18, 10, 0], 'a': []}

def biggest(aDict):
    maxLength = -1
    for keys in aDict:
        if len(aDict[keys]) > maxLength:
            maxLength = len(aDict[keys])
            word = keys
    return word

print(biggest(animals))    
    
    
    