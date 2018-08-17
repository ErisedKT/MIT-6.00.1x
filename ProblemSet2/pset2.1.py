def remainingBalance(balance, annualInterestRate, monthlyPaymentRate):
    
    '''
    balance: the outstanding balance on the credit card
    annualInterestRate: annual interest rate as a decimal
    monthlyPaymentRate: minimum monthly payment rate as a decimal
    '''
    monthlyInterestRate = annualInterestRate / 12.0  # calculating the monthly interest rate
    
    for i in range(1, 13):
        minMonthlyPayment = balance * monthlyPaymentRate  # calculating the minimum payment for the month
        
        unpaidBalance = balance - minMonthlyPayment  # calculating the unpaid balance for the month
        
        balance = unpaidBalance * (1 + monthlyInterestRate)  # calculating the outstanding balance for the month
        
    print('Remaining balance:', round(balance, 2))  # Printing the remaining balance
        
remainingBalance(484, 0.2, 0.04)