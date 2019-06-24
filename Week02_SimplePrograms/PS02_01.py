
def remainingBalance(balance, numberMonths):
    """
    Calculate remaining balance (balance) after a certain number of months (numberMonths). 
    Uses recursive algorithm. The variable numberMonths is decremented to stop the recursive call
    To make it more generalizable it expects these variables in the global scope:
        (annualInterestRate, monthlyPaymentRate, balance)

    Args:
        balance (float):
            balance of the account at month zero

        numberMonths (int):
            number of months over which the interest accumulates

    Returns:
        float:
            final balance
    """

    # when numberMonths reaches zero (base case), it stops the recursive call
    if numberMonths == 0:
        return balance

    # calculate minimum monthly payment
    minimumMonthlyPayment = monthlyPaymentRate * balance

    # calculate the monthly unpaid balance (i.e. residual left on the balance)
    monthlyUnpaidBalance = balance-minimumMonthlyPayment

    # calculate the new balance after the payment
    balance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)

    # decrease the variable that test the condition of the recursive strategy
    numberMonths -= 1

    # recursive call with numberMonths decreased
    return remainingBalance(balance, numberMonths)


# define global scope variables
# annualInterestRate = 0.2       # Monthly interest rate
# monthlyPaymentRate = 0.04      # Minimum monthly payment rate)
# balance = 484                   # Balance
numberMonths = 12              # Number of months over which to calculate the balance

# calculate the monthly interest rate
monthlyInterestRate = annualInterestRate/12.0

# calculate the remianing balance after numberMonths of paying
print('Remaining balance: ', round(remainingBalance(balance, numberMonths), 2))
