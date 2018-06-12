x = 27
low = 0.0
high = x
mid = (low + high)/2.0
numGuesses = 0
epsilon = 0.01
while abs(mid**3 - x) >= epsilon:
    print('low = ', low, 'high = ', high)
    numGuesses += 1
    if mid**3 < x:
        low = mid
    else:
        high = mid
    mid = (low + high)/2.0
print('numGuesses = ', numGuesses)
print(mid, 'is close to cube root of ', x)
        
