# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
extraPayment = 1000
extraPaymentStart = 61
extraPaymentEnd = 108
total_paid = 0.0
months = 0

while principal > 0:
    if months < extraPaymentEnd:
        principal = principal * (1+rate/12) - payment - extraPayment
        total_paid = total_paid + payment + extraPayment
        months = months + 1
        print(months, total_paid, principal)
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        months = months + 1
        print(months, total_paid, principal)

print('Total paid: ', total_paid)
print('Months: ', months)


