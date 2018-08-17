animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    values = aDict.values()
    count = 0
    for ent in values:
        count += len(ent)
    return count

print(how_many(animals))