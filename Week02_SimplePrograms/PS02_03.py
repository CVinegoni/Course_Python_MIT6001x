# Problem 3 - Using Bisection Search to Make the Program Faster
# 20/20 points (graded)
# You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? You can try running your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment is a multiple of $0.01). Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances and interest rates. (Note: when your code is running on our servers, there are limits on the amount of computing time each submission is allowed, so your observations from running this experiment on the grading system might be limited to an error message complaining about too much time taken.)

# Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code? We can make this program run faster using a technique introduced in lecture - bisection search!

# The following variables contain values as described below:

# balance - the outstanding balance on the credit card

# annualInterestRate - annual interest rate as a decimal

# To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance within a year. What is a reasonable lower bound for this payment value? $0 is the obvious answer, but you can do better than that. If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the original balance, so we must pay at least this much every month. One-twelfth of the original balance is a good lower bound.

# What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year. What we ultimately pay must be greater than what we would've paid in monthly installments, because the interest was compounded on the balance we didn't pay off each month. So a good upper bound for the monthly payment would be one-twelfth of the balance, after having its interest compounded monthly for an entire year.


# define global scope variables


# # VERSION 01
# annualInterestRate = 0.2       # Monthly interest rate
# balance = 320000                   # Balance
# numberMonths = 12              # Number of months over which to calculate the balance

# # calculate the monthly interest rate
# monthlyInterestRate = annualInterestRate/12.0

# # calculate lower bound value
# lowerBoundPayment = balance/numberMonths

# # calculate upper bound value
# upperBoundPayment = balance * \
#     ((1 + monthlyInterestRate)**numberMonths)/numberMonths

# # test condition for the wile loop to stop it
# reachedMinimum = False

# originalBalance = balance
# while reachedMinimum == False:
#     # calculate midvalue
#     midValue = round(lowerBoundPayment +
#                      (upperBoundPayment-lowerBoundPayment)/2, 2)
#     # make midvalue such that it is with a second decimal precision
#     midValue = int((lowerBoundPayment +
#                     (upperBoundPayment-lowerBoundPayment)/2)*100)/100

#     # set the minimum montly payment to check at midvalue
#     minimumFixedMonthlyPayment = midValue

#     # set the balance equal to its original value unmodified
#     balance = originalBalance

#     if midValue in [upperBoundPayment, lowerBoundPayment]:
#         break
#     for months in range(1, 13):     # calculate over a year period
#         monthlyUnpaidBalance = balance-minimumFixedMonthlyPayment
#         balance = monthlyUnpaidBalance + monthlyInterestRate*monthlyUnpaidBalance
#     if balance == 0:
#         break
#     elif balance > 0:
#         lowerBoundPayment = midValue
#     elif balance < 0:
#         upperBoundPayment = midValue


# print('Lowest Payment: ', minimumFixedMonthlyPayment)


# VERSION 02

def calculateBalanceAfterOneYear(balance, MonthlyPayment):
    """
    Calculate the total balance after one year

    Args:
        balance (float):
            balance

        MonthlyPayment (float):
            amount of money to pay per month 

    Return:
        balance (float):
            net balance after one year    
    """

    for months in range(1, 13):     # calculate over a year period
        monthlyUnpaidBalance = balance-MonthlyPayment
        balance = monthlyUnpaidBalance + monthlyInterestRate*monthlyUnpaidBalance
    return balance


def calculateLowestPayment(balance, lowerBoundPayment, upperBoundPayment):
    """
    function to calculate lower payment to extinguish debt in recursive way, with function calling itself.
    Use search and divide
    To make it more generalizable it expects these variables in the global scope:
        (annualInterestRate, monthlyPaymentRate, balance)

    Args:
        balance (float):
            balance of the account at month zero

        lowerBoundPayment (float):
            low part of the saerch  and divide interval

        upperBoundPayment (float):
            high part of the search and divide interval


    Returns:
        float:
            the minimum payment to do 
    """

    # trunc the two extremes of the interval
    lowerBoundPayment = round(lowerBoundPayment, 2)
    upperBoundPayment = round(upperBoundPayment, 2)

    # calculate mid values of the interval
    midValue = round(lowerBoundPayment +
                     (upperBoundPayment-lowerBoundPayment)/2, 2)

    # set the minimum montly payment to check at midvalue
    minimumFixedMonthlyPayment = midValue

    # set base case
    if lowerBoundPayment == upperBoundPayment:
        return minimumFixedMonthlyPayment

    if midValue in [lowerBoundPayment, upperBoundPayment]:
        return minimumFixedMonthlyPayment

    # set the balance to the original value
    balance = originalBalance

    balance = calculateBalanceAfterOneYear(balance, minimumFixedMonthlyPayment)

    if balance == 0:
        return minimumFixedMonthlyPayment
    elif balance > 0:
        lowerBoundPayment = midValue
    elif balance < 0:
        upperBoundPayment = midValue

    return calculateLowestPayment(balance, lowerBoundPayment, upperBoundPayment)


annualInterestRate = 0.20    # Monthly interest rate
balance = 320000                   # Balance
numberMonths = 12              # Number of months over which to calculate the balance

# calculate the monthly interest rate
monthlyInterestRate = annualInterestRate/12.0

# calculate lower bound value
lowerBoundPayment = balance/numberMonths

# calculate upper bound value
upperBoundPayment = balance * \
    ((1 + monthlyInterestRate)**numberMonths)/numberMonths

originalBalance = balance
print(calculateLowestPayment(balance, lowerBoundPayment, upperBoundPayment))
