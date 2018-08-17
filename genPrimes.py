def genPrimes():  
    def isPrime(x):
        if x == 2:
            return True
        else:
            for p in primeList:
                if (x % p) == 0:
                    return False
            return True
    primeList = []
    x = 2
    while True:
        if isPrime(x):
            yield x
            primeList.append(x)
        x += 1
