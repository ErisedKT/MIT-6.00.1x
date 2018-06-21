balance = 3926

annualInterestRate = 0.2

initialBalance = balance  # setting a constant initial balance

monthlyInterestRate = annualInterestRate / 12.0  # calculating the monthly interest rate


low = 0
high = (balance * (1 + monthlyInterestRate)**12) / 12.0
mid = (high + low) / 2.0
epsilon = 0.01
numGuesses = 0

def outstanding(bal, minMP):
    month = 1
    while month <= 12:
        remainingBalance = bal - minMP
        bal = remainingBalance * (1 + monthlyInterestRate)
        month += 1
    return round(bal, 2)
    
while abs(outstanding(balance, mid)) >= epsilon:
    if outstanding(balance, mid) > 0:
        low = mid
    else: 
        high = mid
    mid = (low + high) / 2.0
    numGuesses += 1
print('Lowest Payment: ' + str(round(mid, 2)))
print(numGuesses)

