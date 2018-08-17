def largest_prime_factor(n):
    largest_factor = 1
    while n % 2 == 0:
        n /= 2  
    p = 3
    while n != 1:
        while n % p == 0:
            largest_factor = p
            n = n / p
        p += 2
    print(largest_factor)
    return largest_factor

largest_prime_factor(459)
    