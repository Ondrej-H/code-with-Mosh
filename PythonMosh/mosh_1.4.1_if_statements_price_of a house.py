
price = 1000000
has_good_credit = False
down_payment = 0

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f'Down payment is: {down_payment}')