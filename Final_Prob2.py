def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    clone = L[:]
    max_num = max(clone)
    max_times = clone.count(max_num)
    while max_times % 2 == 0:
        while clone.count(max_num) != 0:
            clone.remove(max_num)
        try:
            max_num = max(clone)
            max_times = clone.count(max_num)
        except:
            return None
    return max_num

        