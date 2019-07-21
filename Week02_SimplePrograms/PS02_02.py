
# # Version 01

# # define global scope variables
# annualInterestRate = 0.2       # Monthly interest rate
# balance = 3926                 # Balance
# numberMonths = 12              # Number of months over which to calculate the
#                                # balance

# # calculate the monthly interest rate
# monthlyInterestRate = annualInterestRate/12.0
# originalBalance = balance
# reachedMinimum = False
# for minimumFixedMonthlyPayment in range(10, balance, 10):
#     balance = originalBalance
#     for months in range(1, 13):
#         monthlyUnpaidBalance = balance-minimumFixedMonthlyPayment
#         balance = (monthlyUnpaidBalance + monthlyInterestRate
#                    * monthlyUnpaidBalance
#         if balance < 0:
#             reachedMinimum = True
#             break
#     if reachedMinimum == True:
#         break
# print('zz ', minimumFixedMonthlyPayment)


# Version 02
# define global scope variables
annualInterestRate = 0.2       # Monthly interest rate
balance = 320000                   # Balance
# Number of months over which to calculate the balance
numberMonths = 12

# calculate the monthly interest rate
monthlyInterestRate = annualInterestRate / 12.0

# save original balance into a variable because used as test
originalBalance = balance

# test condition for the wile loop to stop it
reachedMinimum = False

# variable to increment within the while loop
minimumFixedMonthlyPayment = 10

while reachedMinimum is False:

    # every time start loop, reset the balance variable
    balance = originalBalance
    for months in range(1, 13):     # calculate over a year period
        monthlyUnpaidBalance = balance - minimumFixedMonthlyPayment
        balance = (monthlyUnpaidBalance + monthlyInterestRate
                   * monthlyUnpaidBalance)

    # if balance gets negative you found the minimum value
    if balance < 0:
        reachedMinimum = True
    else:
        minimumFixedMonthlyPayment += 10  # increment the while loop variable

print('Lowest Payment: ', minimumFixedMonthlyPayment)
