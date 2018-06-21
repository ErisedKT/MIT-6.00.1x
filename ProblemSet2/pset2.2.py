balance = 3926

annualInterestRate = 0.2

initialBalance = balance  # setting a constant initial balance

monthlyInterestRate = annualInterestRate / 12.0  # calculating the monthly interest rate


for minMonthlyPayment in range(10, initialBalance, 10):
    balance = initialBalance
    month = 1 
    
    while month <= 12:      
        remainingBalance = balance - minMonthlyPayment
        balance = remainingBalance * (1 + monthlyInterestRate)
        month += 1
    
    if balance <= 0:
        print('Lowest Payment:', minMonthlyPayment)
        break
        

