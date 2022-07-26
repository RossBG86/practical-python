# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
extraPayment = 1000
extraPaymentStart = 61
extraPaymentEnd = 108
totalPaid = 0.0
months = 0

while principal > 0:
    if months < extraPaymentEnd:
        principal = principal * (1+rate/12) - payment - extraPayment
        totalPaid = totalPaid + payment + extraPayment
        months = months + 1
        # print(months, total_paid, principal)
        print(f'Months: {months} Total Paid: {totalPaid} Principal: {principal}')
    else:
        principal = principal * (1+rate/12) - payment
        totalPaid = totalPaid + payment
        months = months + 1
        # print(months, total_paid, principal)
        print(f'Months: {months} Total Paid: {totalPaid:0.2f} Principal: {principal:0.2f}')

print(f'Total paid: {totalPaid:0.2f}')
print('Months: ', months)


